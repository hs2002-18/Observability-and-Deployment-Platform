from fastapi import APIRouter, HTTPException
from models.application import Application
from services.application_service import (
    getApplications,
    create_applications,
    get_application_by_id,
    delete_application
)

router = APIRouter()

@router.get("/applications")
def list_applications():
    return getApplications()

@router.post("/applications")
def create_application(app:Application):
    return create_applications(app)

@router.get("/applications/{app_id}")
def get_applications(app_id: int):
    app=get_application_by_id(app_id)
    if app is None:
        raise HTTPException(
            status_code=404,
            detail="Application Not Found"
        )

@router.delete("/applications/{app_id}")
def remove_application(app_id: int):
    return delete_application(app_id)
