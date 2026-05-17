from sqladmin import ModelView
from models.user import User

class UserAdmin(ModelView, model=User):
    name = "пользователя"
    name_plural = "Пользователи"

    column_list = [
        User.id,
        User.email,
        User.last_name,
        User.first_name,
        User.patronymic,
        User.role,
        User.workplace
    ]

    column_labels = {
        User.id: "ID", 
        User.email: "Почта",
        User.last_name: "Фамилия",
        User.first_name: "Имя",
        User.patronymic: "Отчество",
        User.role: "Роль",
        User.workplace: "Место работы"
    }

    column_sortable_list = [
        User.id
    ]

    column_default_sort = [(User.id, True)]

    column_searchable_list = [
        User.id,
        User.email,
        User.last_name
    ]
