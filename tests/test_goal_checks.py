import pytest
from modules.goal_methods import create_goal, get_goals, get_goal, update_goal, delete_goal
import os
from modules.goal_methods import BASE_URL
import requests

@pytest.mark.order(1)
@pytest.mark.steps("Create new Goal")
def test_create_goal():
    response = create_goal()
    assert response.status_code == 200
    goal_id = response.json()["goal"]["id"]  # <-- исправленный путь
    assert goal_id  # Проверка что id получен


@pytest.mark.order(2)
@pytest.mark.steps("Get all Goals")
def test_get_goals():
    response = get_goals()
    assert response.status_code == 200
    assert "goals" in response.json()

@pytest.mark.order(3)
@pytest.mark.steps("Full lifecycle: Create -> Get -> Update -> Delete")
def test_goal_lifecycle():
    with open("goal_id.txt", "r") as f:
        goal_id = f.read().strip()

    get_resp = get_goal(goal_id)
    assert get_resp.status_code == 200

    update_resp = update_goal(goal_id)
    assert update_resp.status_code == 200

    delete_resp = delete_goal(goal_id)
    assert delete_resp.status_code == 200

@pytest.mark.order(4)
@pytest.mark.steps("Try to GET goal with invalid token")
def test_get_with_invalid_token():
    bad_headers = {
        "Authorization": "Bearer WRONGTOKEN"
    }
    url = f"{BASE_URL}/goal/some_id"
    response = requests.get(url, headers=bad_headers)
    print("INVALID TOKEN RESPONSE:", response.status_code, response.text)
    assert response.status_code in [401, 403]

