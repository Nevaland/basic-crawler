import requests


def fetch(url):
    response = requests.get(url)
    return response.text
