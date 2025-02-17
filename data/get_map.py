import requests

from data.config import API_KEY, LL2, LL1, SPN


def get_map():
    map_request = f"https://static-maps.yandex.ru/v1?ll={LL1},{LL2}&spn={SPN}&apikey={API_KEY}"
    response = requests.get(map_request)
    print(response)

    map_file = "maps_folder/map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
