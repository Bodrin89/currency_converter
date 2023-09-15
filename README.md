
# Конвертер валют
___

### стек

+ python3.11 <img height="24" width="24" src="https://cdn.simpleicons.org/python/5066b3" />
+ fastapi <img height="24" width="24" src="https://cdn.simpleicons.org/fastapi/5066b3" />
+ Docker <img height="24" width="24" src="https://cdn.simpleicons.org/docker/5066b3" />
+ poetry<img height="24" width="24" src="https://cdn.simpleicons.org/poetry/" />
+ pytest <img height="24" width="24" src="https://cdn.simpleicons.org/pytest/5066b3" /> 
+ Pydantic 1.1 <img height="24" width="24" src="https://cdn.simpleicons.org/pydantic/5066b3" />
+ mypy
+ Docker-compose

В данном проекте реализован конвертер валют на FastAPI. 
Список не обходимых переменных окружения находится в .env.example



Ознакомиться с версией проекта и документацией можно по ссылке http://vbodrin.tk:8086/docs

## пример запроса: 
  curl -X 'GET' 'http://vbodrin.tk:8086/api/rates?from_=USD&to=RUB&value=1' -H 'accept: application/json'

## Установка:
1. Клонируйте репозиторий с github на локальный компьютер
2. Создайте виртуальное окружение
3. установите poetry командой `pip install poetry` и инициализируйте командой `poetry init`
4. установите зависимости командой `poetry install`
5. Создайте в корне проекта файл в .env и заполните переменными окружения из .env.example
6. Соберите и поднимите docker-контейнер командой `make local-start-docker-compose`
7. Для запуска не в докере используете команду `make start-project`
8. Для запуска тестов используйте команду `make start-test`


- ### SWAGGER: http://vbodrin.tk:8086/docs
