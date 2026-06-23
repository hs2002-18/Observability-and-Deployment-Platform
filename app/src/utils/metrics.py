from prometheus_client import Counter, Gauge

application_requests_total = Counter(
    "application_requests_total",
    "Total Application API Requests"
)

deployment_requests_total = Counter(
    "deployment_requests_total",
    "Total Deployment API Requests"
)

incident_requests_total = Counter(
    "incident_requests_total",
    "Total Incident API Requests"
)

application_count = Gauge(
    "application_count",
    "Current Number of Applications"
)

deployment_count = Gauge(
    "deployment_count",
    "Current Number of Deployments"
)

incident_count = Gauge(
    "incident_count",
    "Current Number of Incidents"
)