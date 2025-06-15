# main.py
from fastapi import FastAPI
from routers import auth, upload, positions, alerts

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(upload.router, prefix="/upload")
app.include_router(positions.router, prefix="/positions")
app.include_router(alerts.router, prefix="/alerts")
