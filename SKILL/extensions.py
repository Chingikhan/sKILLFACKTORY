import requests
import json


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            base_ticker = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}")
        except:
            raise APIException(f'Не удалось получить курс {base}.')

        try:
            quote_ticker = base_ticker.json()['rates'][quote]
        except:
            raise APIException(f'Не удалось получить курс {quote}.')

        try:
            amount = float(amount)
        except:
            raise APIException(f'Не удалось обработать количество {amount}.')

        total_base = quote_ticker * amount
        return round(total_base, 2)
