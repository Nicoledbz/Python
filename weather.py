import requests

api_key = "824b8d7152cad52889bb540a4e007b26"
city = "Orlando"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today's forecast is", description)
temp_min = json.get("main").get("temp_min")
print("The minimun temperature is", temp_min)
temp_max = json.get("main").get("temp_max")
print("The maximun temperature is", temp_max)