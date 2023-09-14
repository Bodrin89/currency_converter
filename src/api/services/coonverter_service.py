import json
import math
import os
import requests
from requests import Response

from src.simbols import symbols

API_KEY = os.getenv('API_KEY')


class ConverterService:

    @classmethod
    def __get_exchange(cls, currency_from: str, currency_to: str) -> Response:
        try:
            url = 'https://api.apilayer.com/fixer/latest'
            params = {'base': 'USD', 'symbols': f'{currency_from},{currency_to}'}
            headers = {'apikey': API_KEY}
            response = requests.get(url, params=params, headers=headers)

            return response
        except Exception as e:
            raise e

    @classmethod
    def convert_currency(cls, currency_from: str, currency_to: str, value: int) -> dict[str: int]:
        if not symbols.get(currency_from):
            return {'message': f'валюта {currency_from} не найдена'}

        if not symbols.get(currency_to):
            return {'message': f'валюта {currency_to} не найдена'}

        try:
            response = cls.__get_exchange(currency_from, currency_to)
            data = response.json()
            currency_1 = data.get('ratesR')[currency_from]
            currency_2 = data.get('rates')[currency_to]
            result = currency_2 * value / currency_1
            round_res = math.floor(result * 1000) / 1000
            return {f'{value} {currency_from} = {round_res} {currency_to}', response.status_code}

        except Exception as e:
            raise e
