from app.core.database import Base, engine
from app.models.user import User


def create_tables():
    if engine is None:
        raise RuntimeError(
            "DATABASE_URL is not configured."
        )

    Base.metadata.create_all(
        bind=engine
    )

    print("Database tables created successfully.")


if __name__ == "__main__":
    create_tables()
