![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
# Бэкенд для сервиса доставки заказов
REST API-сервис для регистрации курьеров, заказов и распределения заказов

## Бизнес-требования:
1) REST API сервиса, методы:
   - загрузка списка курьеров в систему;
   - загрузка списка заказов в всистему;
   - информация о курьерах с параметрами 'offset' b 'limit';
   - информация о курьере по его id;
   - информация о заказе по его id;
   - информация о заказах с параметрами 'offset' b 'limit';
   - отметка переданных заказов выполненными;

2) расчет зарабтной платы и рейтинга курьеров по формуле за переданный в запросе период;
3) rate limiter для сервиса — ограничение нагрузки в 10 RPS на каждый эндпоинт.
При превышении сервис должен отвечать кодом 429;
4) алгоритм распределения заказов по курьерам, методы:
    - метод распределения заказов в начале каждого дня;
    - метод получения уже распределенных заказов.

API сервиса должен соответствовать схеме в файле openapi.json.

## Реализация

- API реализовано с помощью фреймворка FastAPI.
- База данных - PostgreSQL.
- Приложение и PostgreSQL работают в docker контейнерах.

## Стек

- FastAPI
- SQLAlchemy
- Alembic
- PosgreSQL

## Зависимости
В файле requirements.txt

## Запуск
`docker-compose up -d --build`


