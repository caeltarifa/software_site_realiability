from ast import If, Return
from importlib.metadata import requires
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .web_services import get_cities, get_weather

from django.contrib.auth.decorators import login_required

# Create your views here.


import json
@login_required
def home_weatherapp(request):

    params={}
    context = {
        'title' : 'CAEL APP PYTHON  ',
        'cities' : json.dumps([ serialize_city(city) for city in get_cities(params)])
    }
    return render(request, 'home.html', context)

def serialize_city(obj):
    return {
        'country': obj.get('country'),
        'cities': obj.get('cities')
    }

def weather_api(request):
    city = str(request.GET.get('city_backend'))
    if city:
        city=city.split(' - ')[0]
    params_weather={'q':city, 'aqi':'yes', 'key':'80708fe0179e49c084b233206223003'}
    
    weather = get_weather(params_weather)
    return JsonResponse(weather, safe=False)


@login_required
def main(request):
    return render(request, 'weatherapp/main.html', {'title':'SOUTH AMERICA'})

@login_required
def user_info(request):
    return render(request, 'weatherapp/user_info.html', {'title':'SANTIAGO CHILI'})

'''
def home_weatherapp(request):
    # remove these print statements later
    print('\n\nRequest object:', request)
    print('Request object type:', type(request), '\n\n')
    
    #html_tags = ''
    #<h1>This is the Home Page</h1>
    #<h3>Thanks for visiting us</h3>
    #<p>MVT means:</p>
    #<ul>
    #  <li>Model</li>
    #  <li>View</li>
    #  <li>Template</li>
    #</ul>''
    
    response = HttpResponse(html_tags)    # remove these print statements later
    print('Response object:', response)
    print('Response object type:', type(response))
    print('\n\nUser-agent info :', end='')
    print(request.META['HTTP_USER_AGENT'], '\n\n')
   
    return response
'''