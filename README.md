# Тестовое задание

Django проект реализующий REST API.

### Установка

1. Склонировать репозиторий
2. Установить зависимости `pip install -r requirements.txt`
3. Применить миграции базы данных `python manage.py migrate`

### REST API
Приложение реализует API для двух моделей:
`CustomerProfile` - анкета, `Application` - заявка.

В системе существует 3 типа пользователей:

1. Суперпользователь (su)
2. Партнер (pa)
3. Кредитная организация (co)

В таблице ниже приведено соответствие между url, методом запроса, 
необходимыми правами и действием.

| URL                              | HTTP метод    |  Разрешено | Действие                     |
|----------------------------------|:-------------:|------------|------------------------------|
| `/api/customer-profiles/`        | `GET`         | su, pa     | Получение списка анкет       |
| `/api/customer-profiles/`        | `POST`        | su, pa     | Создание анкеты              |
| `/api/customer-profiles/{id}/`   | `GET`         | su, pa     | Получение анкеты по id       |
| `/api/customer-profiles/{id}/`   | `PUT`         | su         | Редактирование анкеты        |
| `/api/customer-profiles/{id}/`   | `DELETE`      | su         | Удаление анкеты              |
| `/api/applications/`             | `GET`         | su, co     | Получение списка заявок      |
| `/api/applications/`             | `POST`        | su, pa     | Создание заявки              |
| `/api/applications/{id}/`        | `GET`         | su, co     | Получение заявки по id       |
| `/api/applications/{id}/`        | `PUT`         | su         | Редактирование заявки        |
| `/api/applications/{id}/`        | `DELETE`      | su         | Удаление заявки              |
| `/api/applications/{id}/send/`   | `POST`        | pa         | Отправка заявки в кред. орг. |
