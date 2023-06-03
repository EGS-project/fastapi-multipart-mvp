'''response schemas '''

from fastapi import UploadFile
from pydantic import BaseModel


class Conversion(BaseModel):
    target_format: str


class ConversionCreate(Conversion):
    pass


class ConversionRead(Conversion):
    link: str
