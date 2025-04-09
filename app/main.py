# app/main.py
import re
import datetime
import os
from typing import Annotated

from anybadge import Color
from fastapi import FastAPI, Response, Depends, Query
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import AfterValidator
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base
from .crud import get_or_create_badge
import anybadge

Base.metadata.create_all(bind=engine)

app = FastAPI()
root = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(root, 'readme.html')) as f:
    index = f.read()


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


@app.get("/", response_class=HTMLResponse)
def docs():
    return HTMLResponse(index)


@app.get("/visitors/{badge_id}")
def get_badge(
    badge_id: str,
    db: Session = Depends(get_db),
    label: Annotated[str, Query(max_length=50)] = "visitors",
    color: Annotated[str, AfterValidator(validate_and_convert_color)] = "green",
):
    badge = get_or_create_badge(db, badge_id)

    badge = anybadge.Badge(label=label, value=str(badge.counter), default_color=color)
    svg = badge.badge_svg_text

    expiry_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)

    headers = {'Cache-Control': 'no-cache,max-age=0,no-store,s-maxage=0,proxy-revalidate',
               'Expires': expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")}

    return Response(content=svg, media_type="image/svg+xml", headers=headers)


@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")
