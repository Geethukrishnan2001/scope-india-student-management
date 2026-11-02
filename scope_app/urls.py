from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
    path('load-states/',views.load_states,name='load_states'),
    path('load-cities/',views.load_cities,name='load_cities'),
    path('password/<int:id>/',views.password,name='password'),
    path('profile/',views.profile,name='profile'),

]