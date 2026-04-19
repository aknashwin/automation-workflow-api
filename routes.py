from fastapi import APIRouter, HTTPException
from models import SensorReading, WorkflowStatus, Alert
from datetime import datetime
from typing import List

router = APIRouter()

# In-memory storage for demo purposes
sensor_readings = []
workflows = {}
alerts = []

# Thresholds for alert generation
THRESHOLDS = {
    "temperature": 80.0,
    "pressure": 10.0,
    "vibration": 5.0
}

@router.get("/")
def root():
    """Health check endpoint."""
    return {
        "status": "online",
        "service": "Automation Workflow API",
        "version": "1.0.0",
        "timestamp": datetime.now()
    }

@router.post("/sensors/reading")
def submit_sensor_reading(reading: SensorReading):
    """
    Submit a sensor reading from a machine.
    Automatically generates alerts if thresholds are exceeded.
    """
    if reading.timestamp is None:
        reading.timestamp = datetime.now()

    sensor_readings.append(reading)
    generated_alerts = []

    # Check thresholds and generate alerts
    checks = {
        "temperature": reading.temperature,
        "pressure": reading.pressure,
        "vibration": reading.vibration
    }

    for metric, value in checks.items():
        if value > THRESHOLDS[metric]:
            severity = "critical" if value > THRESHOLDS[metric] * 1.5 else "warning"
            alert = Alert(
                machine_id=reading.machine_id,
                alert_type=metric,
                severity=severity,
                value=value,
                threshold=THRESHOLDS[metric],
                message=f"{metric.capitalize()} on {reading.machine_id} exceeds threshold: {value} > {THRESHOLDS[metric]}",
                timestamp=datetime.now()
            )
            alerts.append(alert)
            generated_alerts.append(alert)

    return {
        "status": "received",
        "machine_id": reading.machine_id,
        "timestamp": reading.timestamp,
        "alerts_generated": len(generated_alerts),
        "alerts": generated_alerts
    }

@router.get("/sensors/readings")
def get_all_readings():
    """Retrieve all sensor readings."""
    return {
        "total": len(sensor_readings),
        "readings": sensor_readings
    }

@router.get("/sensors/{machine_id}")
def get_machine_readings(machine_id: str):
    """Retrieve all readings for a specific machine."""
    machine_data = [r for r in sensor_readings if r.machine_id == machine_id]
    if not machine_data:
        raise HTTPException(
            status_code=404,
            detail=f"No readings found for machine {machine_id}"
        )
    return {
        "machine_id": machine_id,
        "total_readings": len(machine_data),
        "readings": machine_data
    }

@router.post("/workflow/start")
def start_workflow(workflow_id: str, description: str = "Automation workflow"):
    """Start a new automation workflow."""
    if workflow_id in workflows:
        raise HTTPException(
            status_code=400,
            detail=f"Workflow {workflow_id} already exists"
        )
    workflow = WorkflowStatus(
        workflow_id=workflow_id,
        status="running",
        progress=0.0,
        message=f"Workflow '{description}' started",
        timestamp=datetime.now()
    )
    workflows[workflow_id] = workflow
    return workflow

@router.get("/workflow/{workflow_id}")
def get_workflow_status(workflow_id: str):
    """Get the status of a workflow."""
    if workflow_id not in workflows:
        raise HTTPException(
            status_code=404,
            detail=f"Workflow {workflow_id} not found"
        )
    return workflows[workflow_id]

@router.put("/workflow/{workflow_id}/complete")
def complete_workflow(workflow_id: str):
    """Mark a workflow as completed."""
    if workflow_id not in workflows:
        raise HTTPException(
            status_code=404,
            detail=f"Workflow {workflow_id} not found"
        )
    workflows[workflow_id].status = "completed"
    workflows[workflow_id].progress = 100.0
    workflows[workflow_id].message = "Workflow completed successfully"
    return workflows[workflow_id]

@router.get("/alerts")
def get_alerts(severity: str = None):
    """Retrieve all alerts, optionally filtered by severity."""
    if severity:
        filtered = [a for a in alerts if a.severity == severity]
        return {"total": len(filtered), "alerts": filtered}
    return {"total": len(alerts), "alerts": alerts}