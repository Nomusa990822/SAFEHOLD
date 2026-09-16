from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128,
    )
    display_name: str | None = Field(
        default=None,
        max_length=100,
    )
    language: str = Field(
        default="en",
        max_length=10,
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    email: EmailStr
    display_name: str | None
    language: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
