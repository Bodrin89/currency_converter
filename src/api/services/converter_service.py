import math

import requests
from requests import Response

from src.api.services import API_KEY
from src.config import BASE_CURRENCY, URL
from src.simbols import symbols


class ConverterService:
    def __init__(self, currency_from: str, currency_to: str, value: int):
        self.currency_from = currency_from.upper()
        self.currency_to = currency_to.upper()
        self.value = value

    async def convert_currency(self) -> dict:
        """Конвертация валют"""
        if not symbols.get(self.currency_from):
            return {'message': f'валюта {self.currency_from} не найдена'}

        if not symbols.get(self.currency_to):
            return {'message': f'валюта {self.currency_to} не найдена'}

        try:
            response = await self.get_exchange()
            data = response.json()
            currency_1 = data.get('rates')[self.currency_from]
            currency_2 = data.get('rates')[self.currency_to]
            result = currency_2 * self.value / currency_1
            round_res = math.floor(result * 1000) / 1000
            return {'status_code': response.status_code,
                    'result': f'{self.value} {self.currency_from} = {round_res} {self.currency_to}'}

        except Exception as e:
            raise e

    async def get_exchange(self) -> Response:
        """Получение курса валют со стороннего API"""
        try:
            params = {'base': BASE_CURRENCY, 'symbols': f'{self.currency_from},{self.currency_to}'}
            headers = {'apikey': API_KEY}
            response = requests.get(URL, params=params, headers=headers)

            return response
        except Exception as e:
            raise e
