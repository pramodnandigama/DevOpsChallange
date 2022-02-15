from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1 import api_router

application = FastAPI(title="devops", openapi_url="/api/v1/docs")
application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
application.include_router(api_router, prefix="/api/v1")

