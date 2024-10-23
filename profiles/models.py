from django.db import models
from django.contrib.auth.models import User
from subscriptions.models import StripeCustomer
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user model for maintaining users information

    """

    # add choices for riding style and riding conditions

    RIDING_STYLE_CHOICES = [
        ('Cross Country', 'Cross Country'),
        ('All Mountain', 'All Mountain'),
        ('Downhill', 'Downhill'),
        ('Freeride', 'Freeride'),
    ]

    CONDITIONS_CHOICES = [
        ('Dry', 'Dry'),
        ('Mud', 'Mud'),
        ('Wet', 'Wet'),
        ('Snow', 'Snow'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_active = models.BooleanField(default=False)
    current_subscription = models.ForeignKey(StripeCustomer, null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=20,  null=True, blank=True)
    riding_style = models.CharField(max_length=20, choices=RIDING_STYLE_CHOICES, null=True, blank=True)
    favourite_place_to_ride = models.CharField(max_length=50, null=True, blank=True)
    local_trails = models.CharField(max_length=50, null=True, blank=True)
    bike = models.CharField(max_length=50, null=True, blank=True)
    favourite_conditions = models.CharField(max_length=20, choices=CONDITIONS_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ create or update user profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
