from django.shortcuts import render, redirect
from .models import Trail
from django.contrib.auth.models import User
from subscriptions.models import StripeCustomer
from .forms import TrailForm


def trails(request):
    """Query the database for Trail objects
       Then pass the objects to the trails template
    """
    trails = Trail.objects.all()

    # check if user is subscribed through the subscriptions app
     # Check if the user is subscribed (if they are authenticated)
    user_is_subscribed = False  # Default to not subscribed
    if request.user.is_authenticated:
        try:
            # Retrieve the StripeCustomer object for the user and check subscription status
            stripe_customer = StripeCustomer.objects.get(user=request.user)
            user_is_subscribed = stripe_customer.has_active_subscription()
        except StripeCustomer.DoesNotExist:
            user_is_subscribed = False

    return render(request, 'trails/trails.html', {
      'trails': trails,
      'user_is_subscribed': user_is_subscribed,
    })

def add_trails(request):
    if request.method == 'POST':
        form = TrailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trails')
    else:
        form = TrailForm()
    return render(request, 'trails/add_trail.html', {'form': form})

