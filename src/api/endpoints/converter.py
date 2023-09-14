import math

import requests
from fastapi import APIRouter

from src.api.services.coonverter_service import ConverterService
from src.simbols import symbols

router_api = APIRouter(prefix='/api', tags=['converter'])




@router_api.get('/rates')
def get_exchange(from_: str, to: str, value: int):

    ss = ConverterService.convert_currency(from_, to, value)
    print(ss)
    return ss