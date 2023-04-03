'''router.py is a core of each module with all the endpoints'''

from http import HTTPStatus
import json
from fastapi import APIRouter, FastAPI, File, Depends, Form, Response, UploadFile, Request
from src.conversion.schemas import ConversionCreate

conversion_router = APIRouter()

@conversion_router.post('/api/v1/convert/to-jpeg')
async def convert_to_jpeg(
    conversion_create: ConversionCreate = Depends(ConversionCreate),
    file: UploadFile = File()
    ):

    return Response(
        content=json.dumps({
            'filename' : file.filename,
            'conversion_create' : conversion_create.dict()
            }),
        status_code=HTTPStatus.OK
    )
