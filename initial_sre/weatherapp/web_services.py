import requests

#https://api.weatherapi.com/v1/current.json?key=80708fe0179e49c084b233206223003&q=Santiago&aqi=yes

def generate_request_weather(url, params={}):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()


def get_weather(params={}):
    
    if params=={}:
        params={'q':'Santiago', 'aqi':'yes', 'key':'80708fe0179e49c084b233206223003'}
    url = 'https://api.weatherapi.com/v1/current.json'
    
    response = generate_request_weather(url, params)
    
    if response:
        location = response.get('location')
        current = response.get('current')
        print(location)

        context = {
            'location':location,
            'current':current,
        }

        return context#.get('name')

    return ''




def generate_request_city(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_cities(params={}):
    
    params={}
    url = 'https://countriesnow.space/api/v0.1/countries'
    response = generate_request_city(url, params)
    
    if response:
       location = response.get('data')
       return location

    return 'no city'