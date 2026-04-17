import os
from fastapi import FastAPI, BackgroundTasks
import requests
import uvicorn

app = FastAPI()

CRM_API_KEY = os.getenv("CRM_API_KEY")

@app.get("/")
def home():
    return {"status": "V-Sync Automata Online"}

@app.post("/sync-video")
async def sync_video_to_crm(data: dict, background_tasks: BackgroundTasks):
    video_url = data.get("video_url")
    lead_email = data.get("lead_email")
    background_tasks.add_task(process_sync, video_url, lead_email)
    return {"status": "processing"}

def process_sync(video_url, lead_email):
    # Simulazione logica di sync per attivazione rapida
    print(f"Sincronizzando {video_url} per {lead_email}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
