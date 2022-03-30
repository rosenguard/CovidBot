import requests

class Settings:
    urls = {"germany": "https://api.corona-zahlen.org/germany", "states": "https://api.corona-zahlen.org/states", "vaccinations": "https://api.corona-zahlen.org/vaccinations"}
    
    response = requests.get(urls["germany"])
    response_info = response.json()