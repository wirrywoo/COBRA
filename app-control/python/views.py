from django.shortcuts import HttpResponse
import wandb

from sklearn.linear_model import LogisticRegression
from contextualbandits.online import EpsilonGreedy

cache = {}
version = 'control'
counter = {
    'sum_rewards': 0,
    'num_observations': 0
}

def clicked(request):

    uri = request.META.get('HTTP_REFERER')

    reward = 1 if request.POST.get('clicked') == 'true' else 0

    if isinstance(reward, int) and uri not in cache.keys():

        counter['sum_rewards'] += reward
        counter['num_observations'] += 1

        avg_reward = counter['sum_rewards'] / counter['num_observations']
        cache[uri] = {'version': version, 'avg_reward': avg_reward}
        wandb.init(project = 'cobe-platform', name = version, resume = True)
        wandb.log({"version": version, "avg_reward": avg_reward})
        print(f"URI: {uri}; Version: {version}; Average Reward: {avg_reward}")
    return HttpResponse(reward)
