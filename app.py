import uuid, json, redis, flask

COOKIE_NAME = "sessionID"

def get_session_di():
    