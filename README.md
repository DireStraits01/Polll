# API опросник

Веб-приложение на Django Rest Framework для опроса

## Начало

Эти инструкции позволят вам запустить копию проекта на вашем локальном компьютере.
Применяются следующие технологии: Django 2.2.10, Django REST framework.

### Перед установкой

Для того, чтобы приступить к установке программного обеспечения вам необходимо:

```
   Установить Python3 
   полная инструкция по ссылке
    https://pythonworld.ru/osnovy/skachat-python.html
   
```

### Установка


Пошаговая серия примеров, которые расскажут, как запустить среду разработки.



Создание виртуального окружения

venv
Устанавливать venv не нужно, т.к. он входит в стандартную библиотеку Python. 
Т.е. если вы установили себе Python, то venv у вас уже есть. 
Помните, что venv работает только в Python3!
Для создания виртуального окружения с именем PRG2 с помощью venv
в директории проекта выполните следующую команду:

```
> python -m venv PRG2
```


Активация виртуального окружения в директории проекта на  Linux выполняется командой:
```
>source PRG2/bin/activate
```
на Windows

```
>PRG2\Scripts\activate.bat
```
Установка зависимостей из requirements.txt:

```
pip install -r requirements.txt
```
username: admin
password: 123
## Выполните миграции 

В случае удаления базы даннных

Для Linuxa 

```
python3 manage.py makemigrations
python3 manage.py migrate
```
Для Windowsa
```
python manage.py makemigrations
python manage.py migrate
```
создание суперпользователя:

```
python3 manage.py createsuperuser
```
### документация по DRF API
Перейдите по ссылке  /api/token/, и введите данные ранее зарегстрированого пользователя в ответе придет token (JWT-токен) с пометкой access.
При отправке  токена в заголовке укажите Authorization: Bearer <токен> 

Создать опрос и изменить:
```
/api/polls/
/api/polls/<poll_id>/
```
Добавить вопрос и изменить

```
/api/polls/<poll_id>/questions/
/api/polls/<poll_id>/questions/<question_id>/
```


Добавить варианты ответа

```
/api/polls/<poll_id>/questions/<question_id>/choices/
```

Завершенные опросы

```
/api/my_polls/
```

Пройти опрос

```
/api/polls/<poll_id>/questions/<question_id>/answers/
```

Просмотреть действующие опросы

```
/api/active_polls/
```






