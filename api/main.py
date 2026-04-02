from fastapi import FastAPI
from db.db_initializer import DBInitializer
from db.session import Base, engine
from routers import roles

app = FastAPI()

app.include_router(roles.router, prefix="/roles", tags=["roles"])

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    DBInitializer()
