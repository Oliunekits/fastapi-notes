from fastapi import FastAPI
from app.api.router import api_router
from app.db.database import Base, engine


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    create_db_and_tables()
    app = FastAPI(title="Notes API")
    app.include_router(api_router, prefix="/api")
    return app


app = get_application()


@app.get("/")
def root():
    return {"message": "Notes API is running"}
