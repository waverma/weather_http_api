import argparse
import sys

from api_exception import ApiException
from weather_http_api import get_weather

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', type=str, required=True)
    parser.add_argument('-r', '--range', type=int, default=1)
    args = parser.parse_args()
    try:
        try:
            with open("api_weather.txt") as file:
                api_key = file.read().strip()
        except FileNotFoundError:
            api_key = 'b59a8640cd7bcdab9f102cca06fab3be'

        print('-' * 100)
        for day in get_weather(args.city, args.range, api_key):
            for line in day:
                print(f'{line}: {day[line]}')
            print('-'*100)
    except ApiException as exc:
        print(exc.message)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(0)