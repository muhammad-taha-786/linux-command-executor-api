from fastapi import APIRouter, HTTPException
from utils.executor import run_linux_command

router = APIRouter(prefix="/system", tags=["System Commands"])

@router.get("/uptime")
def get_uptime():
    try:
        output = run_linux_command(["uptime"])
        return {"command": "uptime", "output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/disk")
def get_disk_space():
    try:
        output = run_linux_command(["df", "-h"])
        return {"command": "df -h", "output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/memory")
def get_memory_status():
    try:
        output = run_linux_command(["free", "-m"])
        return {"command": "free -m", "output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user")
def get_current_user():
    try:
        output = run_linux_command(["whoami"])
        return {"command": "whoami", "output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))