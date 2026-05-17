from fastapi import FastAPI
from sqladmin import Admin
from db.session import engine
from admin.views.users import UserAdmin

def setup_admin(app: FastAPI):
    admin = Admin(
        app, 
        engine,
        title="Виртуальный 3D-инженер",
        templates_dir="templates"
    )

    admin.add_view(UserAdmin)
