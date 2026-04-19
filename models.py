from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SensorReading(BaseModel):
    """Represents a sensor reading from a machine on the production line."""
    machine_id: str
    temperature: float
    pressure: float
    vibration: float
    timestamp: Optional[datetime] = None

class WorkflowStatus(BaseModel):
    """Represents the status of an automation workflow."""
    workflow_id: str
    status: str
    progress: float
    message: str
    timestamp: datetime

class Alert(BaseModel):
    """Represents an alert triggered by abnormal sensor readings."""
    machine_id: str
    alert_type: str
    severity: str
    value: float
    threshold: float
    message: str
    timestamp: datetime