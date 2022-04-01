import requests

#https://api.weatherapi.com/v1/current.json?key=80708fe0179e49c084b233206223003&q=Santiago&aqi=yes

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_region(params={}):
    
    params={'q':'Santiago', 'aqi':'yes', 'key':'80708fe0179e49c084b233206223003'}
    url = 'https://api.weatherapi.com/v1/current.json'
    
    response = generate_request(url, params)
    
    if response:
       location = response.get('location')
       return location.get('region')#.get('name')

    return ''