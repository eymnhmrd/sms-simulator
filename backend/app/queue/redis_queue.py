import redis
import json

r = redis.Redis(host="localhost", port=6379, db=0)

QUEUE_NAME = "sms_queue"

def push_to_queue(message_id: str):
    r.rpush(QUEUE_NAME, message_id)

def pop_from_queue():
    return r.lpop(QUEUE_NAME)