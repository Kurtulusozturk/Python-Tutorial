from urllib import response
from webbrowser import get
import requests
import json



location=input("Şehir arayınız:")
endpoint= "link {}".format(location)
response= response.get(endpoint)

def filter_cities(response):
    
    cities=list(filter(lambda x: x.get("location_type")=="City",response))
    return cities

def print_cities(cities):
    for id,city in enumerate(cities):
        print("{}-{}".format(str(id),city.get("title")))

def forecast(woeid):
    endpoint_forecasting="link/{}".format(woeid)
    response=requests.get(endpoint_forecasting)
    response_to_json=json.loads(response.content)
    consolidated_weather=response_to_json("concolidated_weather")
    return consolidated_weather



if response.statues.code==200:
    convert_to_dict=json.loads(response.content)
    cities=filter_cities(convert_to_dict)
    print_cities(cities)
    city_id=int(input("Şehir seç"))
    city_name=cities(city_id)
    city_woeid=city.get("woeid")

    forecasting_result=forecast(city_woeid)
    for weather in consolidated_weather:
            print(
            weather.get("applicable_date"),weather.get("weather_state_name")
    
            )
            print(response_to_json)

print(cities)