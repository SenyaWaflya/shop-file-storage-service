from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.routers.files import files_router

swagger_ui_parameters = {'tryItOutEnabled': True, 'syntaxHighlight': {'activate': True, 'theme': 'nord'}}

app = FastAPI(title='Mobiles shop', swagger_ui_parameters=swagger_ui_parameters)

app.include_router(files_router)


@app.get('/')
def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse('/docs')
