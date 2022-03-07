from pyowm.owm import OWM


owm = OWM('c0779d2b68b69ef6b733d5629c17506f')
mgr = owm.weather_manager()
weather = mgr.weather_at_place('tel aviv').weather
weather.detailed_status
temp_dict_celsius = weather.temperature('celsius')
wind_dict_in_meters_per_sec = weather.wind()
sun_rise = str(weather.sunset_time(timeformat='date'))
sun_set = weather.sunset_time(timeformat='date')


print(
    f"\n{'-'*50}\nThe Current temperature in Tel Aviv is:\n{temp_dict_celsius['temp']} celsius.\nWith a minimum of:{temp_dict_celsius['temp_min']}C and a maximum of:{temp_dict_celsius['temp_max']}C\nClouds covarage:\n{weather.detailed_status}\nWind information:\nWind speed: {wind_dict_in_meters_per_sec['speed']}mps from {wind_dict_in_meters_per_sec['deg']}deg\nSunrise time:{sun_rise}\nSunset time:{sun_set}\n{'-'*50}\n")


""" def user_city():
    while True:
        city_name = input(
            f"{'-'*60}\nPlease write city name to check the wheather\nUse only alphabet and make sure the city name is correct\nPlease indicate city name here: ")
        if not city_name.isalpha():
            continue
        break

    mgr = owm.weather_manager()
    weather = mgr.weather_at_place(f'{city_name}').weather
    weather.detailed_status
    temp_dict_celsius = weather.temperature('celsius')
    wind_dict_in_meters_per_sec = weather.wind()
    sun_rise = str(weather.sunset_time(timeformat='date'))
    sun_set = weather.sunset_time(timeformat='date')
    print('\n')
    print(
        f"\n{'-'*50}\nThe Current temperature in {city_name.capitalize()} is:\n{temp_dict_celsius['temp']} celsius.\nWith a minimum of:{temp_dict_celsius['temp_min']}C and a maximum of:{temp_dict_celsius['temp_max']}C\nClouds covarage:\n{weather.detailed_status}\nWind information:\nWind speed: {wind_dict_in_meters_per_sec['speed']}mps from {wind_dict_in_meters_per_sec['deg']}deg\nSunrise time:{sun_rise}\nSunset time:{sun_set}\n{'-'*50}\n")


user_city()


def wether_forcast():
    while True:
        city_name = input(
            f"{'-'*60}\nPlease write city name to check the wheather\nUse only alphabet and make sure the city name is correct\nPlease indicate city name here: ")
        if not city_name.isalpha():
            continue
        break
    mgr = owm.weather_manager()
    daily_forecast = mgr.forecast_at_place(
        f"{city_name.capitalize()}, interval='3h'").forecast
    print(f"{'-'*60}\nDaily forcast at {city_name.capitalize()}is:\n{daily_forecast}\n{'-'*60}")


wether_forcast()  """
