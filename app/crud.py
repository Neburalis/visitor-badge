# app/crud.py
from sqlalchemy.orm import Session
from .models import BadgeCounter


def get_or_create_badge(db: Session, badge_id: str) -> BadgeCounter:
    # Ищем существующую запись по данному id
    badge = db.query(BadgeCounter).filter(BadgeCounter.id == badge_id).first()
    if badge is None:
        # Если записи нет, создаем новую
        badge = BadgeCounter(id=badge_id, counter=0)
        db.add(badge)
        db.commit()
        db.refresh(badge)

    # Увеличиваем счетчик
    badge.counter += 1
    db.commit()

    return badge
