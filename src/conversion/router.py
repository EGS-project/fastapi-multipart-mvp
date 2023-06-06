'''router.py is a core of each module with all the endpoints'''

import json
from http import HTTPStatus

from fastapi import (APIRouter, Depends, FastAPI, File, Form, Request,
                     Response, UploadFile)
from starlette.responses import JSONResponse

from src.conversion.schemas import ConversionCreate, ConversionRead

router = APIRouter()
import time


@router.post('/api/v1/convert')
async def convert_ok(
    conversion_create: ConversionCreate = Depends(ConversionCreate),
    image: UploadFile = File(),
    ):
    
    conv_read = ConversionRead(
        target_format=conversion_create.target_format,
        link =f'http://loalhost:123123/here_is_your_super_download_link_.{conversion_create.target_format}'
        )
    time.sleep(3)

        
    return Response(
        status_code=HTTPStatus.OK,
        content=conv_read.json()
        )


@router.post('/api/v1/login')
async def login_ok():
    response = Response(status_code=HTTPStatus.OK,content="Authorized.")
    response.set_cookie(
        key="MY_SUPER_COOOKIE",
        path="/",
        domain="localhost", # instead localhost -> .egs-conv.deti
        samesite="lax",
        secure=False,
        httponly=True,
        value="this is my data in the cookie..."
    )
    response.headers["access-control-expose-headers"] = "Set-Cookie"
    return response


@router.post("/api/v1/logout")
async def logout(
    request: Request,
    ):
    response = Response(status_code=200)
    response.delete_cookie(
        key = "MY_SUPER_COOOKIE", 
        domain = "localhost",
        path = '/',
        samesite = "lax",
        secure=False,
        httponly=True
        )
    
    return response



