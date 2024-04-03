from django.urls import path
from.import views
from django.contrib.auth import views as auth_views





urlpatterns = [
    # urls.py
    # Other URL patterns
    # path('home/',views.home,name='home'),
    path('signup/',views.signupPage,name='signupurl'),
    path('register/',views.register,name="registerurl"),
    path("", views.rooms, name="rooms"),
    path("<str:slug>", views.room, name="room"),
]