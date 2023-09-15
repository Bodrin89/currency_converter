import pytest
import requests

from src.api.services import API_KEY
from src.config import BASE_CURRENCY, URL
from src.api.services.converter_service import ConverterService

param_1 = {'from_': 'USD', 'to': 'RuB', 'value': 1}
param_2 = {'from_': 'UsD', 'to': 'RUB', 'value': 2}
param_3 = {'from_': 'USD', 'to': 'RUB', 'value': 0}
param_4 = {'from_': 'USD', 'to': 'RUB', 'value': -1}


class TestConverterService:

    @pytest.mark.parametrize('params', [param_1, param_2, param_3, param_4])
    def test_convert_currency(self, get_client, mocker, params):
        mocker.patch.object(ConverterService, 'get_exchange')
        response_data = {
            'success': True, 'timestamp': 1694724603, 'base': 'USD', 'date': '2023-09-14', 'rates':
                {'USD': 1, 'RUB': 10.0}
        }
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = response_data

        ConverterService.get_exchange.return_value = mock_response
        response = get_client.get('/api/rates', params=params)

        if params == param_1:
            print(params)
            assert response.json() == {'status_code': 200, 'result': '1 USD = 10.0 RUB'}
        if params == param_2:
            assert response.json() == {'status_code': 200, 'result': '2 USD = 20.0 RUB'}
        if params == param_3:
            assert response.json() == {'status_code': 200, 'result': '0 USD = 0.0 RUB'}
        if params == param_4:
            assert response.status_code == 422

    def test_get_exchange(self):
        params = {'base': BASE_CURRENCY, 'symbols': 'USD, RUB'}

        headers = {'apikey': API_KEY}
        resource = requests.get(URL, params=params, headers=headers)
        assert resource.status_code == 200
