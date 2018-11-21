from typing import List

import requests
import collections
import json
from pprint import pprint

Movie = collections.namedtuple('Movie' ,"category, id, url, title, description")


def call_api(data : str):
    movies= []
    r = requests.get(f"http://search.talkpython.fm/api/search?q={data}")
    result = r.json()
    for raw in result.get('results'):
        movies.append(Movie(**raw))

    return movies


