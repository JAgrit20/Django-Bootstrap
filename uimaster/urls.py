from django.urls import path
from uimaster import views

urlpatterns = [
    path('home',views.home, name='home'),
]
