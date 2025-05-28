import requests
from dotenv import dotenv_values
from faker import Faker

fake = Faker()
config = dotenv_values(".env")

# Общий заголовок с токеном авторизации и типом содержимого
headers = {
    "Authorization": config["TOKEN"],
    "Content-Type": "application/json"
}


def create_goal():
    """
    Створює новий Goal з випадковим імʼям.
    """
    body = {
        "name": fake.catch_phrase(),
        "team_id": config["CLICKUP_TEAM_ID"],
        "due_date": None,
        "description": "Autotest Goal",
        "multiple_owners": False
    }
    url = f"{config['BASE_URL']}/team/{config['CLICKUP_TEAM_ID']}/goal"
    return requests.post(url, headers=headers, json=body)


def get_goals():
    """
    Отримує список всіх Goals.
    """
    url = f"{config['BASE_URL']}/team/{config['CLICKUP_TEAM_ID']}/goal"
    return requests.get(url, headers=headers)


def get_goal(goal_id):
    """
    Отримує конкретний Goal за ID.
    """
    url = f"{config['BASE_URL']}/goal/{goal_id}"
    return requests.get(url, headers=headers)


def update_goal(goal_id):
    """
    Оновлює назву Goal.
    """
    updated_body = {
        "name": f"Updated Goal - {fake.word()}",
        "due_date": None,
        "description": "Updated by autotest",
        "multiple_owners": False
    }
    url = f"{config['BASE_URL']}/goal/{goal_id}"
    return requests.put(url, headers=headers, json=updated_body)


def delete_goal(goal_id):
    """
    Видаляє Goal за ID.
    """
    url = f"{config['BASE_URL']}/goal/{goal_id}"
    return requests.delete(url, headers=headers)
