from utils.metrics import application_count

applications = []

def getApplications():
    return applications

def create_applications(app):
    applications.append(app)
    application_count.set(
        len(applications)
    )
    return app

def get_application_by_id(app_id):
    for app in applications:
        if app.id == app_id:
            return app
    return None

def delete_application(app_id):
    for app in applications:
        if app.id == app_id:
            applications.remove(app)
            application_count.set(
                len(applications)
            )
            return {
                "message": "Application Removed"
                }
    return {
        "message": "Application Not Found"
        }
