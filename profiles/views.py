from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, StripeCustomer
from .forms import UserProfileForm
from django.contrib.auth.models import User

def profile(request):
    """ Display users profile """
    user = request.user #get user

    try:
        # Get the user's Stripe subscription status
        stripe_customer = StripeCustomer.objects.get(user=request.user)

        # Determine if the user has an active subscription
        is_subscribed = stripe_customer.has_active_subscription()

    except StripeCustomer.DoesNotExist:
        # If no StripeCustomer exists, the user is not subscribed
        is_subscribed = False

    try: 
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=user) #if a users profile is not created when registered 

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    user_profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profiles.html' 
    context = {
        'is_subscribed': is_subscribed,
        'form': form, 
        'user_profile': user_profile,
        }

    return render(request, template, context)