from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.incident import Incident
from app.models.user import User
from app.routes.auth import get_current_user
from app.schemas.incident import (
    ALLOWED_STATUSES,
    IncidentCreate,
    IncidentResponse,
    IncidentUpdate,
)


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)


@router.post(
    "",
    response_model=IncidentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_incident(
    incident_data: IncidentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    incident = Incident(
        user_id=current_user.id,
        description=incident_data.description,
        incident_date=incident_data.incident_date,
        location=incident_data.location,
        witnesses=incident_data.witnesses,
        status="DRAFT",
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


@router.get(
    "",
    response_model=list[IncidentResponse],
)
def get_incidents(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    incidents = db.scalars(
        select(Incident)
        .where(Incident.user_id == current_user.id)
        .order_by(Incident.created_at.desc())
    ).all()

    return incidents


@router.get(
    "/{incident_id}",
    response_model=IncidentResponse,
)
def get_incident(
    incident_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    incident = db.scalar(
        select(Incident).where(
            Incident.id == incident_id,
            Incident.user_id == current_user.id,
        )
    )

    if incident is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incident not found.",
        )

    return incident


@router.patch(
    "/{incident_id}",
    response_model=IncidentResponse,
)
def update_incident(
    incident_id: int,
    incident_data: IncidentUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    incident = db.scalar(
        select(Incident).where(
            Incident.id == incident_id,
            Incident.user_id == current_user.id,
        )
    )

    if incident is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incident not found.",
        )

    update_data = incident_data.model_dump(
        exclude_unset=True
    )

    if "status" in update_data:
        new_status = update_data["status"]

        if new_status not in ALLOWED_STATUSES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid incident status.",
            )

    for field, value in update_data.items():
        setattr(incident, field, value)

    db.commit()
    db.refresh(incident)

    return incident


@router.delete(
    "/{incident_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_incident(
    incident_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    incident = db.scalar(
        select(Incident).where(
            Incident.id == incident_id,
            Incident.user_id == current_user.id,
        )
    )

    if incident is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incident not found.",
        )

    db.delete(incident)
    db.commit()

    return None
