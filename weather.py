## CS672 - Python Programming
## Kevin C. Buckley
## 10/10/14
##
## -------------------
##  Weather module
## -------------------

import urllib.request
import json
import re
from pprint import pprint

def get_weather(input_string):

    # use regex to get rid of AND or OR strings in string
    input_string = input_string.lower()
    input_string = re.sub('and', '', input_string)
    input_string = re.sub('or', '', input_string)
    
    #input can have spaces, substitue with %20 for url links
    location = re.sub('\s', '%20', input_string)
    
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + location
    
    page = urllib.request.urlopen(weather_url)
    content = page.read()
    content_string = content.decode("utf-8")

    json_data = json.loads(content_string)

    # return the weather for the input search location string
    try:
        weather_text = (json_data["weather"][0]["main"])
        return weather_text
    except KeyError as e:
        return "error"

    
