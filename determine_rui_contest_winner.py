import urllib.request
import json


def main():
    # first, let's get the most recent data
    with urllib.request.urlopen("https://hubmap-link-api.herokuapp.com/hubmap-datasets?format=jsonld") as url:
        data = json.loads(url.read().decode())
        print(data)
