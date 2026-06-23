from utils.metrics import incident_count

incidents=[]

def get_incident():
    return incidents

def create_incident(incident):
    incidents.append(incident)
    incident_count.set(
        len(incidents)
    )
    return incident

def get_incident_by_id(incident_id):
    for incident in incidents:
        if incident.id == incident_id:
            return incident
    return None