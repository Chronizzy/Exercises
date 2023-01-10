import requests


country = 'Netherlands'
city = 'Zwijndrecht'
method = 2
month = 12
year = 2022


url = f" http://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method={method}&month={month}&year={year}"

print(requests.get(url).json())