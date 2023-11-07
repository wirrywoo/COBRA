from django.shortcuts import HttpResponse
# import wandb
import vowpalwabbit
import numpy as np
import random

cache = {}
counter = {
    'sum_rewards': 0,
    'num_observations': 0
}

vw = vowpalwabbit.Workspace("--cb_explore_adf -q UA --quiet --softmax --lambda=10")
nginx_probability = np.array([0.5, 0.5])

def get_context(seed):
    np.random.seed(hash(seed) % 2**32)
    user_age = 30*np.random.rand() + 20 # assume user age is between 20 to 50
    docker_prob = np.random.uniform(0, 1) # higher probability => user carries more strengths in Docker
    ai_prob = np.random.uniform(0, 1) # higher probability => user carries more strengths in AI/ML
    return {
        'age': user_age,
        'docker_prob': docker_prob,
        'ai_prob': ai_prob
    }

def to_vw_example_format(context, actions, cb_label=None):
    if cb_label is not None:
        chosen_action, cost, prob = cb_label
    example_string = ""
    example_string += "shared |User age={} docker_prob={} ai_prob={}\n".format(
        context["age"], context["docker_prob"], context['ai_prob']
    )
    for action in actions:
        if cb_label is not None and action == chosen_action:
            example_string += "0:{}:{} ".format(cost, prob)
        example_string += "|Action web={} \n".format(action)
    # Strip the last newline
    return example_string[:-1]


def sample_custom_pmf(pmf):
    total = sum(pmf)
    scale = 1 / total
    pmf = [x * scale for x in pmf]
    draw = random.random()
    sum_prob = 0.0
    for index, prob in enumerate(pmf):
        sum_prob += prob
        if sum_prob > draw:
            return index, prob

def get_action(vw, context, actions):
    vw_text_example = to_vw_example_format(context, actions)
    pmf = vw.predict(vw_text_example)
    chosen_action_index, prob = sample_custom_pmf(pmf)
    return actions[chosen_action_index], prob


def update_policy(request):

    uri = request.META.get('HTTP_REFERER')
    _, seed = uri.split("?seed=")

    reward = 1 if request.POST.get('clicked') == 'true' else 0
    if isinstance(reward, int) and uri not in cache.keys():
        context = get_context(seed)
        action = request.POST.get('action')
        if action == 'control':
            prob = nginx_probability[0]
        else:
            prob = nginx_probability[1]
        cost = -1 * reward
        vw_format = vw.parse(
                to_vw_example_format(context, ['control', 'treatment'], (action, cost, prob)),
                vowpalwabbit.LabelType.CONTEXTUAL_BANDIT,
            )
        vw.learn(vw_format)
        print("vw.model successfully updated")
        vw.save("./vw.model")

    return HttpResponse(reward)
