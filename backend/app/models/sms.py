from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4

class SMSCreate(BaseModel):
    sender: str
    receiver: str
    message: str

class SMS(SMSCreate):
    id: str
    status: str
    retry_count: int
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def create(data: SMSCreate):
        now = datetime.utcnow()
        return SMS(
            id=str(uuid4()),
            sender=data.sender,
            receiver=data.receiver,
            message=data.message,
            status="CREATED",
            retry_count=0,
            created_at=now,
            updated_at=now
        )