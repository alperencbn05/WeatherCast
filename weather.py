
import requests
import json
from datetime import datetime

def hava_durumu_getir(cityName):
    # Şehiri al ve Türkçe karakterleri düzelt
    replacements = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    cityName = cityName.translate(replacements)
    cityName = cityName.lower().capitalize()


    # API'den hava durumu verilerini al
    # API anahtarınızı buraya ekleyin
    apiKey = "a08101ec9bd043ec810174739253004"
    city = f"{cityName},Turkey"
    baseUrl = "http://api.weatherapi.com/v1/current.json"

    # API isteği yap
    url = baseUrl + "?key=" + apiKey  + "&q=" + city + "&lang=tr"

    response = requests.get(url)
    data = response.json()

    if data["location"]["country"] != "Turkey":
        return None
            
    
    sehir =  data['location']['name']
    sicaklik = str(data['current']['temp_c'])
    tarih =  datetime.now().strftime("%d-%m-%Y %H:%M")
    return tarih, sehir, sicaklik


