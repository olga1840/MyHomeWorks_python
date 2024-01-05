import requests

input_city = input('Введите название города: ')

url = (https://api.openweathermap.org/data/2.5/weather?q={input city}&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru)

response = requests.get(url)

weather_dict = json.response()