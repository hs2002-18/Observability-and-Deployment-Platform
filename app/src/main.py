from fastapi import FastAPI
from api.applications import router as application_router
from api.deployments import router as deployment_router
from api.incidents import router as incident_router

app=FastAPI(
    title="Cloud Native Observability and Deployment Platform"
)
@app.get("/")
def root():
    return{
        "message":"Cloud-Native Observability Platfor"
    }
@app.get("/health")
def health():
    return {
        "message":"UP"
    }

app.include_router(application_router)
app.include_router(deployment_router)
app.include_router(incident_router)