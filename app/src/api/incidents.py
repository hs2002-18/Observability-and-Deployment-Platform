from fastapi import APIRouter, HTTPException
from utils.metrics import incident_requests_total
from models.incident import Incident
from services.incident_services import (
    get_incident,
    create_incident,
    get_incident_by_id
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Incidents"]
)

@router.get("/incidents")
def list_incidents():
    incident_requests_total.inc()
    return get_incidents()


@router.post("/incidents")
def add_incident(incident: Incident):
    incident_requests_total.inc()
    return create_incident(incident)


@router.get("/incidents/{incident_id}")
def get_incident(incident_id: int):
    incident = get_incident_by_id(incident_id)
    incident_requests_total.inc()
    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident