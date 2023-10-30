from django.shortcuts import HttpResponse

cache = {}

def is_ajax(request): # If clicked by the button
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' 

def clicked(request):
    if request.META.get('PATH_INFO') == '/control-response/':
        version = 'control'
    elif request.META.get('PATH_INFO') == '/treatment-response/':
        version = 'treatment'
    else:
        version = None
    uri = request.META.get('HTTP_REFERER')
    if is_ajax(request):
        reward = 1 if request.POST.get('clicked') else 0
    else:
        reward = 0
    if uri not in cache.keys():
        cache[uri] = {'version': version, 'reward': reward}
        print(f"URI: {uri}; Version: {version}; Reward: {reward}")
    return HttpResponse(reward)