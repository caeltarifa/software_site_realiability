from importlib.metadata import requires
from django.shortcuts import render
from django.http import HttpResponse

from .web_services import get_region

from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def home_weatherapp(request):
    params={}
    context = {
        'title' : get_region(params)
    }
    return render(request, 'home.html', context)

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