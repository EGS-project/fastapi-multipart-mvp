'''router.py is a core of each module with all the endpoints'''

from http import HTTPStatus
import json
from fastapi import APIRouter, FastAPI, File, Depends, Form, Response, UploadFile, Request
from src.conversion.schemas import ConversionCreate
from starlette.responses import JSONResponse

conversion_router = APIRouter()


@conversion_router.post('/api/v1/convert')
async def convert(
    conversion_create: ConversionCreate = Depends(ConversionCreate),
    image: UploadFile = File()
):
    file = image.filename  # breakpoint
    conv = conversion_create.dict()
    return JSONResponse(
        content=json.dumps({
            'filename': file,
            'conversion_create': conv
        }),
        status_code=HTTPStatus.OK
    )
