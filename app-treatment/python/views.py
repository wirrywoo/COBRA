from django.shortcuts import HttpResponse
import wandb
import numpy as np

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

cache = {}
version = 'treatment'
counter = {
    'sum_rewards': 0,
    'num_observations': 0
}

def log_response(request):

    uri = request.META.get('HTTP_REFERER')
    _, seed = uri.split("?seed=")

    reward = 1 if request.POST.get('clicked') == 'true' else 0

    if isinstance(reward, int) and uri not in cache.keys():

        counter['sum_rewards'] += reward
        counter['num_observations'] += 1

        avg_reward = counter['sum_rewards'] / counter['num_observations']
        cache[uri] = {'version': version, 'avg_reward': avg_reward}
        context = get_context(seed)

        wandb.init(project = 'cobe-platform', name = version, resume = True)
        wandb.log({"version": version, "avg_reward": avg_reward})
        print(f"Age: {context['age']}; Docker Proficiency: {context['docker_prob']}; AI/ML Proficiency: {context['ai_prob']}; User Response: {reward}")
        print(f"Average Reward for {version} variant: {avg_reward}")
    return HttpResponse(reward)
