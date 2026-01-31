from typing import Annotated

from fastapi import APIRouter, File, Path, Query, UploadFile
from fastapi.responses import StreamingResponse

from src.schemas.files import FilePath
from src.services.files import FilesService

files_router = APIRouter(prefix='/files', tags=['Files'])


@files_router.post('/', summary='Put file to s3')
async def upload(
    file: Annotated[UploadFile, File(description='Загружаемый файл')],
    bot_id: Annotated[str, Query(description='ID бота', examples=['123456789'])],
    user_id: Annotated[str, Query(description='ID пользователя', examples=['123456789'])],
) -> FilePath:
    return await FilesService.upload(file=file, bot_id=bot_id, user_id=user_id)


@files_router.get('/{image_path:path}', summary='Get file from s3')
async def get(image_path: Annotated[str, Path(description='Путь к файлу')]) -> StreamingResponse:
    return await FilesService.get(image_path)
