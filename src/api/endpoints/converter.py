from fastapi import APIRouter, Query
from typing import Annotated
from src.api.services.converter_service import ConverterService

router_api = APIRouter(prefix='/api', tags=['converter'])


@router_api.get('/rates')
async def get_exchange(from_: str, to: str, value: Annotated[int, Query(ge=0)]):
    response = await ConverterService(from_, to, value).convert_currency()
    return response
