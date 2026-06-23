from fastapi import APIRouter, HTTPException
from models.application import Application
from utils.metrics import application_requests_total
from services.application_service import (
    getApplications,
    create_applications,
    get_application_by_id,
    delete_application
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Applications"]
)

@router.get("/applications")
def list_applications():
    application_requests_total.inc()
    return getApplications()

@router.post("/applications")
def create_application(app:Application):
    application_requests_total.inc()
    return create_applications(app)

@router.get("/applications/{app_id}")
def get_applications(app_id: int):
    app=get_application_by_id(app_id)
    application_requests_total.inc()
    if app is None:
        raise HTTPException(
            status_code=404,
            detail="Application Not Found"
        )

@router.delete("/applications/{app_id}")
def remove_application(app_id: int):
    application_requests_total.inc()
    return delete_application(app_id)
