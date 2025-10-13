# ---------------------------------------------------------
# File: TEST REQUEST.py
# Author: Ahtesham Shaikh
# Description: Part of AI Engineer Assignment – Slackbot Content Pipeline
# ---------------------------------------------------------

import requests
import json

url = "http://127.0.0.1:3000/slack/events"

# Simulating a Slack-style message event
payload = {
    "token": "dummy-verification-token",
    "team_id": "T12345",
    "api_app_id": "A12345",
    "event": {
        "type": "message",
        "user": "U12345",
        "text": "Generate a report on AI trends for this week",
        "channel": "C12345"
    },
    "type": "event_callback",
    "event_id": "Ev12345",
    "event_time": 1734030000
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
