from fastapi import APIRouter

from src.api.services.coonverter_service import ConverterService

router_api = APIRouter(prefix='/api', tags=['converter'])


@router_api.get('/rates')
async def get_exchange(from_: str, to: str, value: int):
    response = await ConverterService.convert_currency(from_, to, value)
    return response
