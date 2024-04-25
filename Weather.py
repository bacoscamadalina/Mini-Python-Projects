'''
                                       Built-in API request by city name
'''

import requests
from pprint import pprint


class OpenWeatherMap:
    URL_WEATHER = 'https://api.openweathermap.org/data/2.5/weather'
    API_KEY = '02722d8b0621f649ca69b7ce2e38c157'

    def __init__(self, city_name):
        self.city_name = city_name

    def get_weather_now(self):
        complete_url = f'{self.URL_WEATHER}?appid={self.API_KEY}&q={self.city_name}&units=metric'
        response = requests.get(complete_url)
        weather_data = response.json()
        #pprint(weather_data)
        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            print(f'Weather in {self.city_name} ')
            print(f'Temperature:  {temperature} ')
            print(f'Humidity: {humidity} ')
            print(f'Description: {description} ')
        else:
            print(f'Error : {weather_data.get("message","City not found")}')

    # date despre vant
    def get_wind_details(self):
        response = requests.get(f'{self.URL_WEATHER}?appid={self.API_KEY}&q={self.city_name}&units=metric')
        wind_data = response.json()
        if wind_data['cod'] == 200:
            wind_speed = wind_data['wind']['speed']
            wind_grade = wind_data['wind']['deg']
            gust = wind_data['wind']['gust']
            print(f'Wind speed is: {wind_speed}')
            print(f'Direction of wind: {wind_grade}')
            print(f'Gust:  {gust}')

        else:
            print(f'Error : {wind_data.get("message", "Wind not found")}')



city_name = input('Enter city name: ')
client = OpenWeatherMap(city_name)
client.get_weather_now()
client.get_wind_details()


