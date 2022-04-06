from django.urls import path
from . import views
from .views import weather_api

app_name = 'weatherapp'

urlpatterns = [
    path('', views.main , name='main'),
    path('user_info/', views.user_info, name='user_info'),
    path('weather_api/', views.weather_api, name='weather_api'),

]
