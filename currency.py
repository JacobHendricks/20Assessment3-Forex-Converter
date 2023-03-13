import requests


def convert(con_from, con_to, amount):
    url = f"https://api.exchangerate.host/convert?from={con_from}&to={con_to}&amount={amount}&places=2"
    response = requests.get(url)
    data = response.json()
    return data["result"]


def get_symbols():
    """Retrieve currency 3 letter symbols and put in set"""
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()
    symbols = {sym for sym in data["symbols"]}
    return symbols
