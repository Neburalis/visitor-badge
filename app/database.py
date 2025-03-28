# app/database.py
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # Настройка подключения к БД (укажите свои данные подключения)
# DATABASE_URL = "postgresql://usr:passd@localhost:5432/postgres"
#
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Создаем подключение к базе данных SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
