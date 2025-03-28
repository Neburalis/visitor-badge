# app/main.py
import re
from typing import Annotated

from anybadge import Color
from fastapi import FastAPI, Response, Depends, Query
from fastapi.responses import FileResponse
from pydantic import AfterValidator
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base
from .crud import get_or_create_badge
import anybadge

# Создаем таблицы при старте приложения
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validate_and_convert_color(color: str):
    if re.match(r"^#[0-9a-f]{6}$", color):
        return color

    try:
        return Color[color.upper()].value
    except KeyError:
        raise ValueError(
            "Color must be in the format #RRGGBB or a valid Color enum name"
        )


# Эндпоинт для генерации баннера по переданному id
@app.get("/badge/{badge_id}")
def get_badge(
    badge_id: str,
    db: Session = Depends(get_db),
    label: Annotated[str, Query(max_length=50)] = "visitors",
    color: Annotated[str, AfterValidator(validate_and_convert_color)] = "green",
):
    # Получаем или создаем запись и увеличиваем счетчик
    badge = get_or_create_badge(db, badge_id)

    # Генерируем SVG-баннер
    badge = anybadge.Badge(label=label, value=str(badge.counter), default_color=color)
    svg = badge.badge_svg_text

    # Возвращаем SVG с нужным заголовком Content-Type
    return Response(content=svg, media_type="image/svg+xml")


@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")
