from db.session import SessionLocal
from models.role import Role
from models.user import User
from models.scene import Scene
from models.model import Model
from models.scene_model import SceneModel
from models.quiz import Quiz
from enums.role import RoleName
from enums.scene import SceneName, SceneTitle, SceneDescription
from enums.model import ModelName, ModelTitle, ModelDescription
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
            self.init_model_children()
            self.init_quizzes()
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

    def init_model_children(self):
        children_model = [
            Model(
                id=2,
                name=ModelName.BREATING_VALVE.value,
                title=ModelTitle.BREATING_VALVE.value,
                description=ModelDescription.BREATING_VALVE.value,
                is_draggable=False,
                is_rotatable=False,
                is_assemblable=False,
                is_informational=True,
                parent_id=1
            ),
            Model(
                id=3,
                name=ModelName.MANHOLE_COVER.value,
                title=ModelTitle.MANHOLE_COVER.value,
                description=ModelDescription.MANHOLE_COVER.value,
                is_draggable=False,
                is_rotatable=False,
                is_assemblable=False,
                is_informational=True,
                parent_id=1
            ),
            Model(
                id=4,
                name=ModelName.XLOPUSHA_XP.value,
                title=ModelTitle.XLOPUSHA_XP.value,
                description=ModelDescription.XLOPUSHA_XP.value,
                is_draggable=False,
                is_rotatable=False,
                is_assemblable=False,
                is_informational=True,
                parent_id=1
            )
        ]

        for child in children_model:
            exists = self.db.query(Model).filter(Model.name == child.name).first()
            if not exists:
                self.db.add(child)

        self.db.commit()

    def init_quizzes(self):
        quizzes = [
            Quiz(
                id=1,
                title="Первый тестовый основной тест на основополагающие знания",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas iaculis viverra ultricies. Morbi varius maximus risus, vitae interdum tortor facilisis eget. Proin rhoncus, magna id fermentum venenatis, ligula lacus sollicitudin est, at porttitor diam ligula a turpis. Proin scelerisque magna ac augue ullamcorper consectetur. Pellentesque nibh ligula, pulvinar quis mi id, maximus dapibus felis. Maecenas dignissim maximus turpis in suscipit. Vivamus vitae elit viverra, lacinia turpis quis, lobortis sapien. Cras quam nibh, dignissim sit amet gravida a, tempor ut metus. Maecenas iaculis velit ac placerat eleifend. Integer non luctus nunc. Cras mauris enim, sollicitudin sit amet odio id, vulputate accumsan augue.",
                attempts_count=2,
                questions_count=5,
                time=10,
                scene_id=1
            ),
            Quiz(
                id=2,
                title="Второй тестовый дополнительный тест на расширенные знания",
                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas iaculis viverra ultricies. Morbi varius maximus risus, vitae interdum tortor facilisis eget. Proin rhoncus, magna id fermentum venenatis, ligula lacus sollicitudin est, at porttitor diam ligula a turpis. Proin scelerisque magna ac augue ullamcorper consectetur. Pellentesque nibh ligula, pulvinar quis mi id, maximus dapibus felis. Maecenas dignissim maximus turpis in suscipit. Vivamus vitae elit viverra, lacinia turpis quis, lobortis sapien. Cras quam nibh, dignissim sit amet gravida a, tempor ut metus. Maecenas iaculis velit ac placerat eleifend. Integer non luctus nunc. Cras mauris enim, sollicitudin sit amet odio id, vulputate accumsan augue.",
                attempts_count=1,
                questions_count=3,
                time=5,
                scene_id=1
            ),
        ]

        for quiz in quizzes:
            exists = self.db.query(Quiz).filter(Quiz.title == quiz.title).first()
            if not exists:
                self.db.add(quiz)

        self.db.commit()
