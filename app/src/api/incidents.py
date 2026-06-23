from fastapi import APIRouter, HTTPException

from models.incident import Incident
from services.incident_services import (
    get_incident,
    create_incident,
    get_incident_by_id
)

router = APIRouter()

@router.get("/incidents")
def list_incidents():
    return get_incidents()


@router.post("/incidents")
def add_incident(incident: Incident):
    return create_incident(incident)


@router.get("/incidents/{incident_id}")
def get_incident(incident_id: int):

    incident = get_incident_by_id(incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident