# Get the Location and Weather
import requests
import json
import urllib.request as urllibReq
from bs4 import BeautifulSoup


# Get the location
def ip_location():
    url = 'http://ipinfo.io/json'
    response = urllibReq.urlopen(url)
    data = json.load(response)

    city = data['city']

    with open('user_info/user_city.txt', 'w') as f:
        f.write(city)

    return


# Get and filter the specific link
def links():
    # read city name
    with open('user_info/user_city.txt') as f:
        city_name = f.read()
    soup = BeautifulSoup(requests.get(f'https://uk.search.yahoo.com/search?p={city_name} + India + weather + today + weather.com').content, 'html.parser')
    yahoo_links = []
    for a in soup.find_all('a', href=True):
        word = 'https://weather.com'
        start_index = a['href'].find(word)
        if start_index == 0:
            yahoo_links.append(a['href'])

    return yahoo_links


# Get weather data
def get_weather():
    url = links()
    url = url[0]
    for i in ['tenday', 'hourbyhour']:
        url = url.replace(i, 'today')

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')


    temp_unit = soup.find("span", attrs={"class":"LanguageSelector--unitDisplay--23xY5"}).text.replace("°", "")

    temperature = soup.find("span", attrs={"class": "CurrentConditions--tempValue--3a50n"}).text.replace("°", "")

    description = soup.find("div", attrs={"class": "CurrentConditions--phraseValue--2Z18W"}).text

    humidity = soup.find("span", attrs={"data-testid": "PercentageValue"}).text

    # Check temperature unit and convert it
    if temp_unit == 'F':
        temperature = str(round(((int(temperature) - 32)*5)/9.))

    # Store the weater data
    open('user_info/weather_data.txt', 'w').close()
    for result in [temperature, description, humidity]:
        with open('user_info/weather_data.txt', 'a') as f:
            f.write(result + '\n')



if __name__ == '__main__':
    while True:
        get_weather()

