'''router.py is a core of each module with all the endpoints'''

import json
from http import HTTPStatus

from fastapi import (APIRouter, Depends, FastAPI, File, Form, Request,
                     Response, UploadFile)
from starlette.responses import JSONResponse

from src.conversion.schemas import ConversionCreate, ConversionRead

conversion_router = APIRouter()


@conversion_router.post('/api/v1/convert/ok')
async def convert_ok(
    conversion_create: ConversionCreate = Depends(ConversionCreate),
    image: UploadFile = File(),
):
    
    conv_read = ConversionRead(
        target_format=conversion_create.target_format,
        link =f'http://loalhost:123123/here_is_your_super_download_link_.{conversion_create.target_format}'
        )
        
    return Response(
        status_code=HTTPStatus.OK,
        content=conv_read.json()
        )


@conversion_router.post('/api/v1/convert/bad')
async def convert_bad(
    conversion_create: ConversionCreate = Depends(ConversionCreate),
    image: UploadFile = File(),
):
    # any code that is not 200
    return Response(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content="1000 character exception message"
        )


@conversion_router.get('/api/v1/login/ok')
async def login_ok():
    response = Response(status_code=HTTPStatus.OK,content="Authorized.")
    response.set_cookie(
        key="MY_SUPER_COOOKIE",
        path="/",
        domain="localhost",
        samesite="none",
        secure=True,
        value="this is my data in the cookie..."
    )

    return response


@conversion_router.get('/api/v1/login/bad')
async def login_bad():

    return Response(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content="1000 character exception message"
        )

