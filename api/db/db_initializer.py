from db.session import SessionLocal
from models.role import Role
from models.user import User
from models.scene import Scene
from models.model import Model
from models.scene_model import SceneModel
from enums.role import RoleName
from enums.scene import SceneName, SceneTitle, SceneDescription
from crud.user import get_user_by_email
from services.security_service import SecurityService

class DBInitializer:
    def __init__(self):
        self.db = SessionLocal()
        try:
            self.init_roles()
            self.init_test_user()
            self.init_scenes()
            self.init_models()
            self.init_scenes_models()
        finally:
            self.db.close()

    def init_roles(self):
        roles = [
            Role(id=1, name=RoleName.STUDENT.value),
            Role(id=2, name=RoleName.TEACHER.value),
            Role(id=3, name=RoleName.EMPLOYEE.value),
            Role(id=4, name=RoleName.UNDEFINED.value)
        ]

        for role in roles:
            exists = self.db.query(Role).filter(Role.id == role.id).first()
            if not exists:
                self.db.add(role)

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

    def init_scenes(self):
        scenes = [
            Scene(
                id=1,
                name=SceneName.BARREL.value,
                title=SceneTitle.BARREL.value,
                description=SceneDescription.BARREL.value
            )
        ]

        for scene in scenes:
            exists = self.db.query(Scene).filter(Scene.id == scene.id).first()
            if not exists:
                self.db.add(scene)

        self.db.commit()
    
    def init_models(self):
        models = [
            Model(
                id=1,
                name="Barrel",
                title=SceneTitle.BARREL.value,
                is_draggable=False,
                is_rotatable=False,
                is_assemblable=False,
                is_informational=False,
            )
        ]

        for model in models:
            exists = self.db.query(Model).filter(Model.id == model.id).first()
            if not exists:
                self.db.add(model)

        self.db.commit()

    def init_scenes_models(self):
        scenes_models = [
            SceneModel(
                scene_id=1,
                model_id=1
            )
        ]

        for link in scenes_models:
            exists = (
                self.db.query(SceneModel)
                .filter(SceneModel.scene_id == link.scene_id, SceneModel.model_id == link.model_id)
                .first()
            )
            if not exists:
                self.db.add(link)

        self.db.commit()
