import time

api_key = "fc51dfd03456555e16d19dfa764b1c07"

import requests
from time import sleep

while True:
    pain = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/weather?lat=30.096655&lon=31.662533&appid={api_key}")
    if pain.status_code != 401:
        print("YOU CAN USE IT NOW")
    else:
        print("NOPE")
    time.sleep(5)
