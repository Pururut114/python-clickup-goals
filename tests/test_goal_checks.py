import pytest
from modules.goal_methods import create_goal, get_goals, get_goal, update_goal, delete_goal
from dotenv import dotenv_values
import requests

config = dotenv_values(".env")


@pytest.mark.order(1)
@pytest.mark.steps("Create new Goal")
def test_create_goal():
    """
    Створення Goal та перевірка відповіді.
    """
    response = create_goal()
    assert response.status_code == 200
    yield  # Для покрокового отображения в отчёте CI
    goal_id = response.json()["id"]
    assert goal_id is not None


@pytest.mark.order(2)
@pytest.mark.steps("Get all Goals")
def test_get_goals():
    """
    Отримання всіх Goals.
    """
    response = get_goals()
    assert response.status_code == 200
    yield
    assert isinstance(response.json()["goals"], list)


@pytest.mark.order(3)
@pytest.mark.steps("Full lifecycle: Create -> Get -> Update -> Delete")
def test_goal_lifecycle():
    """
    Повний життєвий цикл: створення, отримання, оновлення, видалення Goal.
    """
    # Створення
    create_resp = create_goal()
    assert create_resp.status_code == 200
    goal_id = create_resp.json()["id"]
    yield "Created goal"

    # Отримання
    get_resp = get_goal(goal_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == goal_id
    yield "Fetched goal"

    # Оновлення
    update_resp = update_goal(goal_id)
    assert update_resp.status_code == 200
    yield "Updated goal"

    # Видалення
    delete_resp = delete_goal(goal_id)
    assert delete_resp.status_code == 200
    yield "Deleted goal"


@pytest.mark.order(4)
@pytest.mark.steps("Try to GET goal with invalid token")
def test_get_with_invalid_token():
    """
    GET-запит з неправильним токеном повинен повернути статус 401.
    """
    invalid_headers = {
        "Authorization": "invalid_token",
        "Content-Type": "application/json"
    }
    url = f"{config['BASE_URL']}/team/{config['CLICKUP_TEAM_ID']}/goal"
    response = requests.get(url, headers=invalid_headers)
    yield
    assert response.status_code == 401
