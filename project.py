import requests, sys, re, datetime, os
from urllib.parse import urlencode

appId = os.getenv("OPEN_WEATHER_APP_ID")

def get_forecast(lat, lon, units):
    base_url = 'https://api.openweathermap.org/data/3.0/onecall'
    params = {
        'appid': appId,
        'lat': lat,
        'lon': lon,
        'units': units,
        'exclude': 'minutely,hourly,alerts'
    }

    encoded_params = urlencode(params)

    try:
        result = requests.get(f'{base_url}?{encoded_params}')
        result.raise_for_status()

        return result.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def get_location(locationCriteria):
    base_url = 'https://api.openweathermap.org/geo/1.0/direct'
    params = {
        'appid': appId,
        'q': ','.join(locationCriteria),
        'limits': 1
    }

    encoded_params = urlencode(params)

    try:
        result = requests.get(f'{base_url}?{encoded_params}')
        result.raise_for_status()

        return result.json()
    except requests.RequestException as e:
        print(f"Can not get the location: {e}")
        return None


def amount_of_days():
    while True:
        days = input("\nPlease type amount of days you are interested in (from 1 to 8): ")

        if is_numeric_and_in_range(days):
            break
    return int(days)

def messurment_unit():
    while True:
        units = input("\nChoose units of measurement. Type 1 for metric or 2 for imperial system: ")
        if units == "1":
            unit = "metric"
            break
        if units == "2":
            unit = "imperial"
            break
    return unit

def is_country_code_valid(code):
    return bool(re.match(r'^[A-Z]{2,3}$', code))

def is_numeric_and_in_range(value):
    if value.isdigit():
        numeric_value = int(value)
        if 1 <= numeric_value <= 8:
            return True
    return False


def location_input():
    location = []
    while True:
        city = input("\nEnter the name of the City: ")
        if len(city):
            location.append(city)
            break

    while True:
        countryCode = input("\nEnter the country code (ISO 3166) or we will try our best to guess it: ")
        if len(countryCode) == 0 or is_country_code_valid(countryCode):
            location.append(countryCode)
            break

    if countryCode == 'US' or countryCode == 'USA':
        stateCode = input("\nEnter the state code (only for US): ")
        location.insert(1, stateCode)

    return list(filter(None, location))

def handle_forecast_data(location, days, data,unit):
    if unit == "metric":
        degrees = "°C"
        speed = "m/s"
    else:
        degrees = "°F"
        speed = "mph"

    title = f"Forecast for {location['name']}, {location['country']}"

    if 'state' in location:
        title +=f" ,{location['state']}"

    print("")
    print(title)
    for index, day in enumerate(data['daily']):
        if index < days:
            print("")
            date_time = datetime.datetime.fromtimestamp((day['dt']))
            print(f"{date_time.day}.{date_time.month}.{date_time.year}:")
            print(f"Summary: {day['summary']}")
            print(f"Temperature is: {day['temp']['day']}{degrees}")
            print(f"Wind speed is: {day["wind_speed"]} {speed}")

def main():
    print("Welcome to the Weather Forecast")

    location = get_location(location_input())

    if not location or len(location) == 0:
        sys.exit('Location has not been found')

    lat = location[0]['lat']
    lon = location[0]['lon']

    unit = messurment_unit()

    days = amount_of_days()

    forecast_data = get_forecast(lat, lon, unit)

    handle_forecast_data(location[0], days, forecast_data, unit)


if __name__ == "__main__":
    main()
