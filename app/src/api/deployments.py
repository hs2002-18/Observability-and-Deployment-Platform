from fastapi import APIRouter, HTTPException
from utils.metrics import deployment_requests_total
from models.deployment import Deployment
from services.deployment_services import(
    get_deployments,
    create_deployment,
    get_deployment_by_id
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Deployments"]
)

@router.get("/deployments")
def list_deployments():
    deployment_requests_total.inc()
    return get_deployments()

@router.post("/deployments")
def add_deployment(deployment: Deployment):
    deployment_requests_total.inc()
    return create_deployment(deployment)

@router.get("/deployments/{deployment_id}")
def get_deployment(deployment_id: int):
    deployment = get_deployment_by_id(deployment_id)
    deployment_requests_total.inc()
    if deployment is None:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found"
        )
    return deployment