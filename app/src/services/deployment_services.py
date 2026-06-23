from utils.metrics import deployment_count

deployments = []

def get_deployments():
    return deployments

def create_deployment(deployment):
    deployments.append(deployment)
    deployment_count.set(
        len(deployments)
    )
    return deployment

def get_deployment_by_id(deployment_id):
    for deployment in deployments:
        if deployment.id == deployment_id:
            return deployment
    return None
