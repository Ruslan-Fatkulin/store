from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/<int:pk>', views.about, name='about')
]
