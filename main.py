from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.api.storage.client import init_bucket
from src.routers.files import files_router

swagger_ui_parameters = {'tryItOutEnabled': True, 'syntaxHighlight': {'activate': True, 'theme': 'nord'}}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    _ = app
    init_bucket()
    yield


app = FastAPI(title='Mobiles shop', swagger_ui_parameters=swagger_ui_parameters, lifespan=lifespan)

app.include_router(files_router)


@app.get('/')
def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse('/docs')
