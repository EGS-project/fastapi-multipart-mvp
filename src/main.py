'''main.py is a root of the project, which inits the FastAPI app'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.conversion.router import conversion_router

app = FastAPI(openapi_url="/api/v1/openapi.yaml")
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost:8000", "*"],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=['*']
    )
    
app.include_router(router=conversion_router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8888,
        reload=True,
    )
