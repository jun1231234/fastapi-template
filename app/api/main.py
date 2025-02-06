from fastapi import APIRouter
from .routes import test, chat

api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
