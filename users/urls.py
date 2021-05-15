from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('extendedSignup', views.extendedSignup, name='extendedSignup'),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path('checkout', views.checkout, name='checkout'),
    path('create_sub', views.create_sub, name='create_sub'),
    path('complete', views.complete, name='complete'),
]