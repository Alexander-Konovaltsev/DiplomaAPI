from db.session import SessionLocal
from models.role import Role

class DBInitializer:
    def __init__(self):
        self.db = SessionLocal()
        try:
            self.init_roles()
        finally:
            self.db.close()

    def init_roles(self):
        roles = [
            {"id": 1, "name": "Студент"},
            {"id": 2, "name": "Преподаватель"},
            {"id": 3, "name": "Сотрудник предприятия"},
            {"id": 4, "name": "Прочее"},
        ]

        for role in roles:
            exists = self.db.query(Role).filter(Role.id == role["id"]).first()
            if not exists:
                self.db.add(Role(**role))

        self.db.commit()
