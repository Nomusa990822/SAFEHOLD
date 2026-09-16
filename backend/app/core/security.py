from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from jose import jwt

from app.core.config import settings


password_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return password_hasher.hash(password)


def verify_password(
    password: str,
    password_hash: str,
) -> bool:
    try:
        password_hasher.verify(
            password_hash,
            password,
        )
        return True
    except Exception:
        return False


def create_access_token(
    subject: str,
    expires_minutes: int | None = None,
) -> str:
    if expires_minutes is None:
        expires_minutes = settings.access_token_expire_minutes

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=expires_minutes
    )

    payload = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )
