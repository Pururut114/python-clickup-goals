import os
import requests
from dotenv import load_dotenv
from faker import Faker

load_dotenv()

BASE_URL = os.environ["BASE_URL"]
TEAM_ID = os.environ["CLICKUP_TEAM_ID"]
TOKEN = os.environ["CLICKUP_TOKEN"]

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

fake = Faker()

def create_goal():
    url = f"{BASE_URL}/team/{TEAM_ID}/goal"
    payload = {
        "name": "Autotest Goal",
        "description": "Created during pytest",
        "due_date": None,
        "multiple_owners": False,
        "owners": [],
        "color": "#32a852"
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    print("CREATE GOAL RESPONSE:", response.status_code, response.text)
    if response.status_code == 200:
        goal_id = response.json()["goal"]["id"]
        with open("goal_id.txt", "w") as f:
            f.write(goal_id)
    return response

def get_goals():
    url = f"{BASE_URL}/team/{TEAM_ID}/goal"
    return requests.get(url, headers=HEADERS)

def get_goal(goal_id):
    url = f"{BASE_URL}/goal/{goal_id}"
    return requests.get(url, headers=HEADERS)

def update_goal(goal_id):
    url = f"{BASE_URL}/goal/{goal_id}"
    payload = {
        "name": "Updated Goal Name",
        "description": "Updated via test",
        "due_date": None,
        "color": "#123456",
        "add_owners": [],
        "rem_owners": []
    }
    return requests.put(url, headers=HEADERS, json=payload)

def delete_goal(goal_id):
    url = f"{BASE_URL}/goal/{goal_id}"
    return requests.delete(url, headers=HEADERS)
