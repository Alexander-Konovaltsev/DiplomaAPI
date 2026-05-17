from fastapi import FastAPI, APIRouter
from db.db_initializer import DBInitializer
from db.session import Base, engine
from routers import (
    roles, 
    users, 
    scenes, 
    models,
    models_views, 
    quizzes, 
    results, 
    questions, 
    results_details
)
from admin.admin import setup_admin
from admin.router import router as admin_router

app = FastAPI()

api_router = APIRouter(prefix="/api")

api_router.include_router(roles.router)
api_router.include_router(users.router)
api_router.include_router(scenes.router)
api_router.include_router(models.router)
api_router.include_router(models_views.router)
api_router.include_router(quizzes.router)
api_router.include_router(results.router)
api_router.include_router(questions.router)
api_router.include_router(results_details.router)

app.include_router(api_router)
app.include_router(admin_router)

setup_admin(app)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    DBInitializer()
