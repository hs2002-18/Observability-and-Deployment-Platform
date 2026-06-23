from fastapi import APIRouter, HTTPException

from models.deployment import Deployment
from services.deployment_services import(
    get_deployments,
    create_deployment,
    get_deployment_by_id
)

router = APIRouter()

@router.get("/deployments")
def list_deployments():
    return get_deployments()

@router.post("/deployments")
def add_deployment(deployment: Deployment):
    return create_deployment(deployment)

@router.get("/deployments/{deployment_id}")
def get_deployment(deployment_id: int):
    deployment = get_deployment_by_id(deployment_id)
    if deployment is None:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found"
        )
    return deployment