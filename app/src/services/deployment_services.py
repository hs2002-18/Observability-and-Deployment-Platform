deployments = []

def get_deployments():
    return deployments

def create_deployment(deployment):
    deployments.append(deployment)
    return deployment

def get_deployment_by_id(deployment_id):
    for deployment in deployments:
        if deployment.id == deployment_id:
            return deployment
    return None
