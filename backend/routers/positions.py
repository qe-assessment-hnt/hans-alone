# routers/positions.py
from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_positions():
    # TODO: return user positions from DB
    return {"positions": []}