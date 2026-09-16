from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


ALLOWED_STATUSES = {
    "DRAFT",
    "PRIVATE",
    "SHARED",
    "EXPORTED",
    "REPORTED",
}


class IncidentCreate(BaseModel):
    description: str = Field(
        min_length=1,
        max_length=10000,
    )

    incident_date: datetime | None = None

    location: str | None = Field(
        default=None,
        max_length=255,
    )

    witnesses: str | None = Field(
        default=None,
        max_length=5000,
    )


class IncidentUpdate(BaseModel):
    description: str | None = Field(
        default=None,
        min_length=1,
        max_length=10000,
    )

    incident_date: datetime | None = None

    location: str | None = Field(
        default=None,
        max_length=255,
    )

    witnesses: str | None = Field(
        default=None,
        max_length=5000,
    )

    status: str | None = Field(
        default=None,
        max_length=20,
    )


class IncidentResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    description: str
    incident_date: datetime | None
    location: str | None
    witnesses: str | None
    status: str
    created_at: datetime
    updated_at: datetime
