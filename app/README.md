# API Documentation

## Base URL

```http
http://localhost:8000
```

---

## Health Check

### Get Health Status

```http
GET /health
```

Response

```json
{
  "status": "UP"
}
```

---

## Applications API

### Create Application

```http
POST /api/v1/applications
```

Request Body

```json
{
  "id": 1,
  "name": "payment-service",
  "environment": "dev",
  "status": "running"
}
```

### Get All Applications

```http
GET /api/v1/applications
```

### Get Application By ID

```http
GET /api/v1/applications/{id}
```

### Delete Application

```http
DELETE /api/v1/applications/{id}
```

---

## Deployments API

### Create Deployment

```http
POST /api/v1/deployments
```

Request Body

```json
{
  "id": 1,
  "application": "payment-service",
  "version": "1.0.0",
  "status": "success"
}
```

### Get All Deployments

```http
GET /api/v1/deployments
```

### Get Deployment By ID

```http
GET /api/v1/deployments/{id}
```

---

## Incidents API

### Create Incident

```http
POST /api/v1/incidents
```

Request Body

```json
{
  "id": 1,
  "service": "payment-service",
  "severity": "critical",
  "status": "open"
}
```

### Get All Incidents

```http
GET /api/v1/incidents
```

### Get Incident By ID

```http
GET /api/v1/incidents/{id}
```

---

## Metrics

### Prometheus Metrics

```http
GET /metrics
```

Available Metrics

### Counters

```text
application_requests_total
deployment_requests_total
incident_requests_total
```

### Gauges

```text
application_count
deployment_count
incident_count
```