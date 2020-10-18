import json

import requests

from limehometest.settings import HERE_PLACES_BASE_URL, HERE_API_KEY


class HerePlacesApi:
    def __init__(self):
        pass

    def near_coordinates(self, at):
        response = requests.get(f'{HERE_PLACES_BASE_URL}discover/explore/',
                                dict(at=at, cat='accommodation', apiKey=HERE_API_KEY))
        data = json.loads(response.content)
        return data.get('results', {}).get('items', [])
