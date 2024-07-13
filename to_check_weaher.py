

import requests
def get_weather(weather_name):
    url = f"http://wttr.in/{user_input}?format=%C+%t"
    res = requests.get(url)
    if res.status_code == 200:
        print(f"Weather in {weather_name}: {res.text.strip()}")
    else:
        print("City not found")  
while True:
    user_input = input("Enter the city name: ").lower()
    get_weather(user_input)