import requests
import os

curAbbrev = {
    'USD': 1,
    'GBP': 2,
    'EUR': 3,
    'CHF': 4,
    'RUB': 5,
    'KRW': 16,
    'CAD': 20,
}


def get_item(appid, name, currency='EUR'):
    r"""
    Function from: https://github.com/MatyiFKBT/PySteamMarket
    Gets item listings from the `Steam Marketplace`.
    @appid ID of game item belongs to.
    @name: Name of item to lookup.

    @currency: Abbreviation of currency to return listing prices in.
    Accepted currencies:`USD,GBP,EUR,CHF,RUB,KRW,CAD`

    Defaults to `EUR`.
    Please lookup the proper abbreviation for your currency of choice.

    Returns a json object
    Example:
    ```
    {
        "success": true,
        "lowest_price": "0,92€",
        "volume": "15",
        "median_price": "0,80€"
    }
    ```
    """
    url = 'https://steamcommunity.com//market/priceoverview'
    market_item = requests.get(url, params={
        'appid': appid,
        'market_hash_name': name,
        'currency': curAbbrev[currency]
    })
    return market_item.json()


def get_item_history(appid: int, name: str, currency: str = 'EUR') -> []:
    r"""
        Function inspired from: https://github.com/MatyiFKBT/PySteamMarket
        Gets item price history from the `Steam Marketplace`.
        @appid ID of game item belongs to.
        @name: Name of item to lookup.
        @currency: Abbreviation of currency to return listing prices in.
        Accepted currencies:`USD,GBP,EUR,CHF,RUB,KRW,CAD`

        Defaults to `EUR`.
        Please lookup the proper abbreviation for your currency of choice.

        Returns a json object
        Example:
        ```
        {
            "success": true,
            "price_prefix": "",
            "price": "€",
            "prices": "[
            ["Aug 10 2014 01: +0",11.605,"1159"],
            ["Aug 11 2014 01: +0",11.65,"1100"],
            ...,
            ]"
        }
        ```
        """
    url = 'https://steamcommunity.com/market/pricehistory'
    cookie = {'steamLoginSecure': os.environ.get('STEAM_LOGIN_COOKIES')}

    market_item_history = requests.get(url, cookies=cookie, params={
        'appid': appid,
        'market_hash_name': name,
        'currency': curAbbrev[currency]
    })
    return market_item_history.json()

