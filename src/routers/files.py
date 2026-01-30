from fastapi import APIRouter, UploadFile

from src.schemas.files import FileInfo
from src.services.files import FilesService

files_router = APIRouter(prefix='/files', tags=['Files'])


@files_router.post('/', summary='Put file to s3')
async def upload(file: UploadFile, bot_id: str, user_id: str) -> FileInfo:
    return await FilesService.upload(file=file, bot_id=bot_id, user_id=user_id)


@files_router.post('/url', summary='Generate presigned url from s3')
async def get_image_url(image_path: str) -> str:
    return await FilesService.get_image_url(image_path)
