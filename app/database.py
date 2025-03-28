# app/database.py
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # Настройка подключения к БД (укажите свои данные подключения)
# DATABASE_URL = "postgresql://usr:passd@localhost:5432/postgres"
#
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Создаем подключение к базе данных SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./db.sqlite")

engine = create_engine(
    DATABASE_URL,
    connect_args=(
        {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
    ),
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
