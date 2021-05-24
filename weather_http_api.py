from datetime import date

import requests

from api_exception import ApiException


def get_weather(city, days_count, api_key):
    if days_count > 7 or days_count < 1:
        print('Invalid days count. Might be between 0 and 8.')
        return
    response = None
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}')
        lon = response.json()['coord']['lon']
        lat = response.json()['coord']['lat']
        url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={api_key}'
        response = requests.get(url).json()['daily']

        for i in range(days_count):
            result = {}
            day_info = response[i]

            result['Date'] = date.fromtimestamp(day_info["dt"])
            result['Morn'] = f'{round(day_info["temp"]["morn"], 1)}°C, feels like {round(day_info["feels_like"]["morn"], 1)}°C'
            result['Day'] = f'{round(day_info["temp"]["day"], 1)}°C, feels like {round(day_info["feels_like"]["day"], 1)}°C'
            result['Night'] = f'{round(day_info["temp"]["night"], 1)}°C, feels like {round(day_info["feels_like"]["night"], 1)}°C'
            result['Humidity'] = f'{day_info["humidity"]}%'
            result['Wind speed'] = f'{day_info["wind_speed"]} m/s'
            result['Weather'] = f'{day_info["weather"][0]["main"]} ({day_info["weather"][0]["description"]})'

            yield result

    except KeyError:
        raise ApiException(response.json()['message'])
