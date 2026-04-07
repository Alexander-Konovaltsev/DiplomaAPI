from db.session import SessionLocal
from models.role import Role
from models.user import User
from crud.user import get_user_by_email
from services.security_service import SecurityService

class DBInitializer:
    def __init__(self):
        self.db = SessionLocal()
        try:
            self.init_roles()
            self.init_test_user()
        finally:
            self.db.close()

    def init_roles(self):
        roles = [
            {"id": 1, "name": "Студент"},
            {"id": 2, "name": "Преподаватель"},
            {"id": 3, "name": "Сотрудник"},
            {"id": 4, "name": "Прочее"},
        ]

        for role in roles:
            exists = self.db.query(Role).filter(Role.id == role["id"]).first()
            if not exists:
                self.db.add(Role(**role))

        self.db.commit()

    def init_test_user(self):
        email = "test@test.ru"

        if get_user_by_email(self.db, email):
            return
        
        test_user = User(
            last_name="Тестовый",
            first_name="Тест",
            patronymic="Тестович",
            email=email,
            password=SecurityService.hash_password("1234"),
            role_id=1,
            workplace="Тестовый университет"
        )

        self.db.add(test_user)
        self.db.commit()
