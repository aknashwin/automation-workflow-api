# Automation Workflow API

A REST API simulating an industrial automation workflow system with real-time sensor monitoring, threshold-based alert generation, and workflow management. Built with FastAPI and Python.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-orange?style=flat)
![Uvicorn](https://img.shields.io/badge/Uvicorn-4051B5?style=flat)

## 📋 Overview

This project demonstrates a production-style REST API that simulates industrial automation workflows. It provides endpoints for:

- Submitting and retrieving machine sensor readings
- Automatic alert generation when readings exceed safety thresholds
- Severity tiering — warnings vs critical alerts
- Starting, monitoring and completing automation workflows
- Fully interactive API documentation via Swagger UI

Designed to simulate real-world industrial IoT pipelines used in manufacturing, robotics, and automation environments.

## 🖥️ Interactive API Documentation

FastAPI auto-generates a live Swagger UI documentation page. Once running, visit:

```
http://127.0.0.1:8000/docs
```

All endpoints are fully testable directly in the browser — no external tools needed.

## 🛠️ Tech Stack

- **Python** — Core language
- **FastAPI** — Modern, high-performance web framework
- **Uvicorn** — ASGI server for running the API
- **Pydantic** — Data validation and schema definition

## 📁 Project Structure

```
automation-workflow-api/
│
├── main.py               # FastAPI app entry point
├── routes.py             # All API endpoint definitions
├── models.py             # Pydantic data models
└── requirements.txt      # Project dependencies
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/aknashwin/automation-workflow-api.git
cd automation-workflow-api
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API
```bash
python -m uvicorn main:app --reload
```

### 5. Open the docs
Navigate to **http://127.0.0.1:8000/docs** in your browser.

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/` | Health check |
| `POST` | `/api/v1/sensors/reading` | Submit a sensor reading |
| `GET` | `/api/v1/sensors/readings` | Get all sensor readings |
| `GET` | `/api/v1/sensors/{machine_id}` | Get readings for a specific machine |
| `POST` | `/api/v1/workflow/start` | Start a new workflow |
| `GET` | `/api/v1/workflow/{workflow_id}` | Get workflow status |
| `PUT` | `/api/v1/workflow/{workflow_id}/complete` | Complete a workflow |
| `GET` | `/api/v1/alerts` | Get all alerts (filterable by severity) |

## ⚙️ Alert Thresholds

| Metric | Warning Threshold | Critical Threshold |
|---|---|---|
| Temperature | > 80.0°C | > 120.0°C |
| Pressure | > 10.0 bar | > 15.0 bar |
| Vibration | > 5.0 mm/s | > 7.5 mm/s |

## 📊 Example Request & Response

**Submit a sensor reading:**
```json
POST /api/v1/sensors/reading
{
  "machine_id": "MACHINE-001",
  "temperature": 95.0,
  "pressure": 8.0,
  "vibration": 3.0
}
```

**Response:**
```json
{
  "status": "received",
  "machine_id": "MACHINE-001",
  "alerts_generated": 1,
  "alerts": [
    {
      "machine_id": "MACHINE-001",
      "alert_type": "temperature",
      "severity": "warning",
      "value": 95.0,
      "threshold": 80.0,
      "message": "Temperature on MACHINE-001 exceeds threshold: 95.0 > 80.0"
    }
  ]
}
```

## 🔮 Future Improvements

- Add PostgreSQL database for persistent storage
- Implement authentication with JWT tokens
- Add WebSocket support for real-time sensor streaming
- Build a dashboard frontend for live monitoring
- Deploy to cloud (AWS/Azure) with Docker
