from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def subscribe(request):
    return render(request, 'subscribe/subscribe.html')

