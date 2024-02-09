# Приложение QRKot

## Project Description

An API application for raising funds for charity projects. \
All users may see charity projects. Only registered users may make untied donations which automatically go to opened charity projects (First In, First Out). Only superusers may create or update charity projects.


## Installation
- Clone the repository
  ```
  git clone https://github.com/TatianaBelova333/cat_charity_fund.git
  ```
- Install all dependencies and activate virtual enironment
  ```
  python -m venv venv
  ```
  ```
  pip install -r requirements.txt
  ```
- Create an .env file as in the env.example file.

- Run migrations for SQLite
  ```
  alembic upgrade head
  ```

- Run the application:
  ```
  uvicorn app.main:app --reload
  ```

## Documenation

http://127.0.0.1:8000/docs - Swagger docs.
http://127.0.0.1:8000/redoc - ReDoc docs.



### Authors
[Tatiana Belova](https://github.com/TatianaBelova333)
