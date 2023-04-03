'''response schemas '''

from fastapi import UploadFile
from pydantic import BaseModel


class Conversion(BaseModel):
    format: str
    size: int
    
class ConversionCreate(Conversion):
    pass

class ConversionRead(Conversion):
    link: str
