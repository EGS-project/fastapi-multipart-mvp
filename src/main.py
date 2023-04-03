'''main.py is a root of the project, which inits the FastAPI app'''

from fastapi import FastAPI
import uvicorn
from src.conversion.router import conversion_router

app = FastAPI(openapi_url="/api/v1/openapi.yaml")
    
    
app.include_router(router=conversion_router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8888,
        reload=True,
    )
