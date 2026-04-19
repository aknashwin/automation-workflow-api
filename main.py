from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Automation Workflow API",
    description="""
    A REST API simulating an industrial automation workflow system.
    
    ## Features
    * **Sensor Monitoring** — Submit and retrieve machine sensor readings
    * **Threshold Alerts** — Automatic alert generation when readings exceed safe limits
    * **Workflow Management** — Start, monitor and complete automation workflows
    * **Severity Tiering** — Alerts classified as warning or critical based on severity
    
    Built to simulate real-world industrial IoT and automation pipelines.
    """,
    version="1.0.0",
    contact={
        "name": "Ashwin Nair",
        "url": "https://github.com/aknashwin",
        "email": "ashwinkanair@gmail.com"
    }
)

app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    print("Automation Workflow API is running!")
    print("Docs available at: http://127.0.0.1:8000/docs")