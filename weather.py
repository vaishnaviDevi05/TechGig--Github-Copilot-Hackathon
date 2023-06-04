# get command line input from user for country variable
strCountry = input("Enter a country: ")
# use OpenWeatherMap API to get weather data for country
# use API key "4ed87fa9625d7ef538af355a6827447f"
# use metric units
# print the weather data
# print the temperature in degrees Celsius
# print the humidity
# print the wind speed in km/h
# print the weather description
# print the name of the city
def getWeather(strCountry):
    import requests
    import json
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + strCountry + "&appid=4ed87fa9625d7ef538af355a6827447f&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    print("The temperature in " + strCountry + " is " + str(data["main"]["temp"]) + " degrees Celsius.")
    print("The humidity in " + strCountry + " is " + str(data["main"]["humidity"]) + "%.")
    print("The wind speed in " + strCountry + " is " + str(data["wind"]["speed"]) + "km/h.")
    print("The weather description in " + strCountry + " is " + str(data["weather"][0]["description"]) + ".")
    print("The name of the city in " + strCountry + " is " + str(data["name"]) + ".")
getWeather(strCountry)