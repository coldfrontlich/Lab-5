#Помогаев Максим 2 вариант
import requests as rg

TOKEN = "7d447d5d5152f8d630947f0187f9c2c5"
def get_weather(city):
    response = rg.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=en&appid={TOKEN}&units=metric')
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    show_weather(city, temp, humidity, wind)

def show_weather(city, temp, humidity, wind):
    print(f"{city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind} m/s")

def get_covid_info(date):
    response = rg.get(f'https://api.covidtracking.com/v1/us/{date}.json')
    data = response.json()
    deathIncrease = data['deathIncrease']
    death = data['death']
    hospIncrease = data['hospitalizedIncrease']
    hosp = data['hospitalized']
    show_covid_info(deathIncrease, death, hospIncrease, hosp)

def show_covid_info(deathIncrease, death, hospIncrease, hosp):
    print(f'Died on this day: {deathIncrease}')
    print(f'Total deaths: {death}')
    print(f'Got sick that day: {hospIncrease}')
    print(f'Sick all the time: {hosp}')
        
        
    

response = rg.get('https://covidtracking.com/data/api')
print(response)

city = input("Input city name: ")
get_weather(city)

date = input("Input date YYYYMMDD: ")
get_covid_info(date)





