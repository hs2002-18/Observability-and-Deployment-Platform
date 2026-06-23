applications = []

def getApplications():
    return applications

def create_applications(app):
    applications.append(app)
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
            return {
                "message": "Application Removed"
                }
    return {
        "message": "Application Not Found"
        }
