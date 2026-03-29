from fastapi import FastAPI
from app.api import sms

app = FastAPI(title="Mini SMSC DevOps Project")

app.include_router(sms.router)