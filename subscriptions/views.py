from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@login_required
def subscribe(request):
    return render(request, 'subscribe/subscribe.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publickey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)