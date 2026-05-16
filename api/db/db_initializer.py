from db.session import SessionLocal
from models.role import Role
from models.user import User
from models.scene import Scene
from models.model import Model
from models.scene_model import SceneModel
from models.quiz import Quiz
from models.question_type import QuestionType
from models.question import Question
from models.answer import Answer
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
            self.init_questions_types()
            self.init_questions()
            self.init_answers()
        finally:
            self.db.close()

    def init_roles(self):
        roles = [
            Role(name=RoleName.STUDENT.value),
            Role(name=RoleName.TEACHER.value),
            Role(name=RoleName.EMPLOYEE.value),
            Role(name=RoleName.UNDEFINED.value)
        ]

        for role in roles:
            exists = self.db.query(Role).filter(Role.name == role.name).first()
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
                name=SceneName.BARREL.value,
                title=SceneTitle.BARREL.value,
                description=SceneDescription.BARREL.value
            )
        ]

        for scene in scenes:
            exists = self.db.query(Scene).filter(Scene.name == scene.name).first()
            if not exists:
                self.db.add(scene)

        self.db.commit()
    
    def init_models(self):
        models = [
            Model(
                name="Barrel",
                title=SceneTitle.BARREL.value,
                is_draggable=False,
                is_rotatable=False,
                is_assemblable=False,
                is_informational=False,
            )
        ]

        for model in models:
            exists = self.db.query(Model).filter(Model.name == model.name).first()
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
                title="Тестирование знаний основных конструктивных элементов РВСП-5000",
                description="Данный тест предназначен для оценки уровня теоретических знаний по устройству, конструкции и основным технологическим элементам резервуара РВСП-5000. В ходе тестирования проверяется понимание назначения ключевых узлов, принципов их работы и особенностей эксплуатации оборудования. Материалы теста охватывают базовые сведения, необходимые для подготовки специалистов, работающих с вертикальными стальными резервуарами.",
                attempts_count=2,
                questions_count=5,
                time=1,
                scene_id=1
            ),
            Quiz(
                title="Расширенное тестирование по устройству, эксплуатации и технологическим системам РВСП-5000",
                description="Данный тест предназначен для углублённой проверки знаний, связанных с конструкцией, эксплуатацией и техническими особенностями резервуара РВСП-5000. Вопросы охватывают дополнительные аспекты функционирования оборудования, назначение вспомогательных систем и принципы взаимодействия отдельных технологических узлов. Тестирование ориентировано на специалистов, обладающих базовой подготовкой и стремящихся подтвердить расширенный уровень профессиональных компетенций.",
                attempts_count=1,
                questions_count=3,
                time=2,
                scene_id=1
            ),
        ]

        for quiz in quizzes:
            exists = self.db.query(Quiz).filter(Quiz.title == quiz.title).first()
            if not exists:
                self.db.add(quiz)

        self.db.commit()

    def init_questions_types(self):
        questions_types = [
            QuestionType(
                name="MultipleChoice"
            ),
            QuestionType(
                name="SingleChoice"
            )
        ]

        for question_type in questions_types:
            exists = self.db.query(QuestionType).filter(QuestionType.name == question_type.name).first()
            if not exists:
                self.db.add(question_type)

        self.db.commit()

    def init_questions(self):
        questions = [
            Question(
                question_text="Какие из перечисленных объектов находятся на сцене?",
                quiz_id=1,
                question_type_id=1
            ),
            Question(
                question_text="Какое из определений устройства хлопуша ХП является верным?",
                quiz_id=1,
                question_type_id=2
            ),
            Question(
                question_text="Для чего предназначены дыхательные клапаны?",
                quiz_id=1,
                question_type_id=1
            ),
            Question(
                question_text="Какое из определений РВСП-5000 является верным?",
                quiz_id=1,
                question_type_id=2
            ),
            Question(
                question_text="Дополните определение: ... — это конструктивный элемент промышленного оборудования, представляющий собой герметичное отверстие с крышкой, которое монтируется в стенках или крышах резервуаров, ёмкостей, аппаратов, цистерн, колодцев и других замкнутых пространств. Его главная функция — обеспечить безопасный и удобный доступ персонала внутрь конструкции для выполнения различных работ.",
                quiz_id=1,
                question_type_id=2
            )
        ]

        for question in questions:
            exists = self.db.query(Question).filter(Question.question_text == question.question_text).first()
            if not exists:
                self.db.add(question)
        
        self.db.commit()

    def init_answers(self):
        answers = [
            Answer(
                text="Паровая турбина",
                question_id=1
            ),
            Answer(
                text="Люк-лаз",
                question_id=1,
                is_correct=True
            ),
            Answer(
                text="Подъемный кран",
                question_id=1
            ),
            Answer(
                text="Дыхательный клапан",
                question_id=1,
                is_correct=True
            ),

            Answer(
                text="Хлопуша ХП — это механический элемент, предназначенный для передачи крутящего момента и компенсации угловых деформаций между узлами конструкции.",
                question_id=2
            ),
            Answer(
                text="Хлопуша ХП — это разъёмный тип крепления трубопроводов или валов, обеспечивающий герметичность и возможность быстрого демонтажа системы.",
                question_id=2
            ),
            Answer(
                text="Хлопуша ХП — это устройство, устанавливаемое внутри вертикального резервуара на приёмо‑раздаточном патрубке для обеспечения операций налива и слива нефтепродукта, а также для дополнительной защиты от его утечки в случае повреждения трубопровода или неисправности запорной арматуры.",
                question_id=2,
                is_correct=True
            ),
            Answer(
                text="Хлопуша ХП — это сборочная единица, включающая подшипник и элементы его крепления, обеспечивающая поддержку вращающегося вала и снижение трения.",
                question_id=2
            ),

            Answer(
                text="Для сокращения потерь нефти от испарения",
                question_id=3,
                is_correct=True
            ),
            Answer(
                text="Для аварийного слива нефтепродукта",
                question_id=3
            ),
            Answer(
                text="Для отвода статического электричества с корпуса резервуара",
                question_id=3
            ),
            Answer(
                text="Для регулирования давления в газовом пространстве или вакуума вертикальных резервуаров",
                question_id=3,
                is_correct=True
            ),
            Answer(
                text="Для очистки поступающего воздуха от влаги",
                question_id=3
            ),

            Answer(
                text="РВСП-5000 — специальная ёмкость для хранения вязких нефтепродуктов при повышенной температуре. Внутри резервуара располагаются электрические нагревательные секции.",
                question_id=4
            ),
            Answer(
                text="РВСП-5000 — накопительная ёмкость для промежуточного хранения топлива во время технического обслуживания трубопроводов. Оснащается системой быстрого опорожнения.",
                question_id=4
            ),
            Answer(
                text="РВСП-5000 — технологический узел для подачи сырья в установки низкотемпературной дистилляции. Обеспечивает автоматическое регулирование потоков вещества.",
                question_id=4
            ),
            Answer(
                text="РВСП-5000 — представляет собой вертикальный цилиндрический резервуар со стационарным покрытием. Предназначен для измерения объёма, а также приёма, хранения и отпуска нефти и нефтепродуктов.",
                question_id=4,
                is_correct=True
            ),

            Answer(
                text="Инспекционный клапан",
                question_id=5
            ),
            Answer(
                text="Люк-лаз",
                question_id=5,
                is_correct=True
            ),
            Answer(
                text="Контрольный шлюз",
                question_id=5
            ),
            Answer(
                text="Смотровой патрубок",
                question_id=5
            ),
        ]

        for answer in answers:
            exists = self.db.query(Answer).filter(Answer.text == answer.text).first()
            if not exists:
                self.db.add(answer)
        
        self.db.commit()
