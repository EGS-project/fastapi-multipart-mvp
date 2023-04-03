

from http import HTTPStatus
from fastapi import Response

from src.conversion.schemas import ConversionRead


class ResponseFactory:
    def __init__(self) -> None:
        pass
    
    def conversion_response(self) -> Response:
        conversion_read = ConversionRead(
            format = 'jpeg',
            size = 123,
            link ='asdasdsa.com/asdasd/asdadf'
        )
        
        return Response(status_code=HTTPStatus.OK, content=conversion_read.json())
    
    