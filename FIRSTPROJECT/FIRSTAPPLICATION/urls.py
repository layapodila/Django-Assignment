from django.urls import path
from FIRSTAPPLICATION import views

urlpatterns = [
    path('', views.index),
    path('member', views.member),
]