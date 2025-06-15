# routers/upload.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import csv

router = APIRouter()

@router.post("")
def upload_csv(file: UploadFile = File(...), product_type: str = Form(...)):
    if product_type not in ["equity", "option", "fx"]:
        raise HTTPException(status_code=400, detail="Invalid product type")

    contents = file.file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(contents)
    records = list(reader)
    # TODO: route to correct parser based on product_type
    return {"status": "success", "product_type": product_type, "records": len(records)}