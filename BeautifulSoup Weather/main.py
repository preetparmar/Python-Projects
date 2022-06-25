# Importing Libraries
import requests
from bs4 import BeautifulSoup

# Function for getting the weather
def get_weather() -> str:
    """ Search the input from the user in google and provide with the weather """

    # Setting the header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Get the city name
    city = input('Enter city name: ')

    # Generating the url
    search_string = city.replace(',', '%2C').replace(' ', '').strip() + '+weather'
    url = f'https://www.google.com/search?client=firefox-b-d&q={search_string}'

    # Requesting the result
    res = requests.get(url=url, headers=headers)

    if res.status_code == 200:
        try:
            soup = BeautifulSoup(res.text, 'html.parser')
            city_name = soup.select('#wob_loc')[0].getText().strip()    # City
            local_time = soup.select('#wob_dts')[0].getText().strip()   # Local Time
            weather = soup.select('#wob_dc')[0].getText().strip()   # Weather Description
            temp_c = soup.select('#wob_tm')[0].getText().strip() + '°C' # Weather in Celcius
            temp_f = soup.select('#wob_ttm')[0].getText().strip() + '°F'    # Weather in Farenheit
            precipitaion = soup.select('#wob_pp')[0].getText().strip()  # Precipitation
            humidity = soup.select('#wob_hm')[0].getText().strip()  # Humidity
            wind_km = soup.select('#wob_ws')[0].getText().strip()   # Wind Speed in km/h
            wind_m = soup.select('#wob_tws')[0].getText().strip()   # Wind Speed in mph

            print(f"""
                Searching on Google...\n
                {city_name}
                {local_time}
                {weather}: {temp_c} | {temp_f}
                Precipitation: {precipitaion}
                Humidity: {humidity}
                Wind Speed: {wind_km} | {wind_m}
                """)
        except:
            print(f"Sorry can't find weather for the '{city}' city.")
    else:
        print(f"Sorry can't find weather for the provided '{city}' city.")

if __name__ == '__main__':
    get_weather()