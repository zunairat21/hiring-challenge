import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def log_step(job_id:str, step:str, success:bool, message:str):
    entry = {
        "job_id" : job_id,
        "step" : step,
        "success": success,
        "message" : message,
        "timestamp" : datetime.utcnow().isoformat() + "Z"
    }

    log_file = LOG_DIR / f"{job_id}.log.json"
    with open(log_file, "a") as fh:
        fh.write(json.dumps(entry) + "\n")
    print(f"[LOG] {entry}")
