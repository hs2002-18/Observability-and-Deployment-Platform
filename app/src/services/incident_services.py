incidents=[]

def get_incident():
    return incidents

def create_incident(incident):
    incidents.append(incident)
    return incident

def get_incident_by_id(incident_id):
    for incident in incidents:
        if incident.id == incident_id:
            return incident
    return None