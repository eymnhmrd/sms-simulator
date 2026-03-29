from fastapi import APIRouter, HTTPException
from app.models.sms import SMSCreate, SMS
from app.services.store import SMS_STORE

router = APIRouter()

@router.post("/sms")
def send_sms(payload: SMSCreate):
    sms = SMS.create(payload)

    # store it
    SMS_STORE[sms.id] = sms

    return {
        "message": "SMS accepted",
        "sms_id": sms.id
    }


@router.get("/sms/{sms_id}")
def get_sms(sms_id: str):
    sms = SMS_STORE.get(sms_id)

    if not sms:
        raise HTTPException(status_code=404, detail="SMS not found")

    return sms