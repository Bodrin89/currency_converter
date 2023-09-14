
import uvicorn
from fastapi import FastAPI

from src.api.endpoints.converter import router_api

app = FastAPI()

app.include_router(router_api)

if __name__ == '__main__':
    uvicorn.run('src.main:app', host='localhost', port=8000, reload=True)
