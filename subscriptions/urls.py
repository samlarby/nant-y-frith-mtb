from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscriptions-subscribe'),
    path('stripe_config/', views.stripe_config, name="stripe_config"),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('webhook/', views.stripe_webhook, name="webhook"),
]

