from django.shortcuts import render, redirect, get_object_or_404
from .models import Trail, TrailFeatureImage
from django.contrib.auth.models import User
from subscriptions.models import StripeCustomer
from .forms import TrailForm, TrailFeatureImageFormSet


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
        feature_image_formset = TrailFeatureImageFormSet(request.POST, request.FILES,
                                                        queryset=TrailFeatureImage.objects.none())

        if form.is_valid() and feature_image_formset.is_valid():
            form.save()

            for feature_image_form in feature_image_formset:
                feature_image = feature_image_form.save(commit=False)
                feature_image.trail = trail
                feature_image.save()
            return redirect('trails')

    else:
        form = TrailForm()
        feature_image_formset = TrailFeatureImageFormSet(queryset=TrailFeatureImage.objects.none())
    return render(request, 'trails/add_trail.html', {
        'form': form,
        'feature_image_formset': feature_image_formset})

def edit_trail(request, trail_id):
    trail = get_object_or_404(Trail, id=trail_id)

    if request.method == 'POST':
        form = TrailForm(request.POST, request.FILES, instance=trail)
        feature_image_formset = TrailFeatureImageFormSet(request.POST, request.FILES,
                                                        queryset=trail.feature_images.all())  # Get existing images
        
        if form.is_valid and feature_image_formset.is_valid():
            form.save()
            
            for feature_image_form in feature_image_formset:
                feature_image = feature_image_form.save(commit=False)
                feature_image.trail = trail  # Ensure the image is linked to the correct trail
                feature_image.save()

            return redirect('trails')
            
    else:
        form = TrailForm(instance=trail)
        feature_image_formset = TrailFeatureImageFormSet(queryset=trail.feature_images.all())  # Load existing images


    return render(request, 'trails/edit_trail.html', {
        'form': form, 
        'trail': trail,
        'feature_image_formset': feature_image_formset
        })

def delete_trail(request, trail_id):
    trail = get_object_or_404(Trail, id=trail_id)

    if request.method == 'POST':
        trail.delete()
        return redirect('trails')
    
    return render(request, 'trails/delete.trail.html', {'trail': trail})

