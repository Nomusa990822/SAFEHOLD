from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    pass


if settings.database_url:
    engine = create_engine(
        settings.database_url,
        pool_pre_ping=True,
    )
else:
    engine = None


SessionLocal = (
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
    if engine
    else None
)


def get_db():
    if SessionLocal is None:
        raise RuntimeError(
            "DATABASE_URL is not configured."
        )

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
