import requests

def get_weather_desc_and_temp():
    api_key = "824b8d7152cad52889bb540a4e007b26"
    city = "Orlando"
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}

def main():
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is", weather_dict.get('description'))
    print("The minimun temperature is", weather_dict.get('temp_min'))
    print("The maximun temperature is", weather_dict.get('temp_max'))


main()