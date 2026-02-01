from typing import Annotated

from pydantic import BaseModel, Field


class FilePath(BaseModel):
    file_path: Annotated[str, Field(description='путь к файлу', examples=['b4b599af-be99-4e3e-acd0-8c7ad5ad6119'])]
