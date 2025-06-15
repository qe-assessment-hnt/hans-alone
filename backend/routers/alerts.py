# routers/alerts.py
from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_alerts():
    # TODO: return active alerts
    return {"alerts": []}
