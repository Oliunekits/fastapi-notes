from fastapi import APIRouter
from app.api.notes import router as notes_router

api_router = APIRouter()

api_router.include_router(notes_router, prefix="/notes", tags=["Notes"])
