import sys
import requests
import json
# get command line input from user for country variable
country = sys.argv[1]
# use openWeatherMap API to get weather data
# use if else to handle internet connection
# use try except to handle errors
# parse JSON data
# print weather data
# print temperature in degrees Celsius
# print humidity
# print wind speed in km/h
# print weather description
# print name of city
def getWeather(country):
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + country + "&appid=4ed87fa9625d7ef538af355a6827447f&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)
        print("The temperature in " + country + " is " + str(data["main"]["temp"]) + " degrees Celsius.")
        print("The humidity in " + country + " is " + str(data["main"]["humidity"]) + "%.")
        print("The wind speed in " + country + " is " + str(data["wind"]["speed"]) + "km/h.")
        print("The weather description in " + country + " is " + str(data["weather"][0]["description"]) + ".")
        print("The name of the city in " + country + " is " + str(data["name"]) + ".")
    except requests.exceptions.ConnectionError:
        print("No internet connection.")
    except KeyError:
        print("Country not found.")
# call function getWeather
getWeather(country)