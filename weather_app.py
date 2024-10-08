import requests
import json
city=input("enter name of a city : ")
API_key="49130f34668b1e3a16565be82a8b4edf"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=49130f34668b1e3a16565be82a8b4edf"
r=requests.get(url)
print(type(r.text))
wdic=json.loads((r.text))
print(f"the temprature in {city} is",wdic["main"]["temp"])
# print(f"the weather is ",wdic["weather"]["main"])
print(f"the {city} is in ",wdic["sys"]['country'])
