import requests

BASE_URL = 'https://ru.yougile.com/api-v2/'
API_TOKEN = "dSvWC4Q86f+Ly8moznYgjnbXiEXrpoQOCIZtvcOPAxcKvh7Vwo1v21KOlHqPpY3P"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
    }

test_project_data = {
    "title": "Мой проект из автотеста"
    }
test_project_none = {
    "title": ""
}

project_id = "0303c2bc-006a-40e0-bd0d-580d509e290e"

test_project_new_name = {
    "title": "Мой проект из автотеста"
}


def test_create_project_positive():
    response = requests.post(
        f"{BASE_URL}/projects",
        json=test_project_data,
        headers=HEADERS
    )

    assert response.status_code == 201


def test_create_project_negative():
    response = requests.post(
        f"{BASE_URL}/projects",
        json=test_project_none,
        headers=HEADERS
    )

    assert response.status_code == 400


def test_get_project_id_positive():
    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )

    assert response.status_code == 200


def test_get_project_id_negativ():
    response = requests.get(
        f"{BASE_URL}/projects/21212",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_put_project_id_positive():
    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json=test_project_new_name,
        headers=HEADERS
    )

    assert response.status_code == 200


def test_put_project_id_negative():
    response = requests.put(
        f"{BASE_URL}/projects/1212121212",
        json=test_project_new_name,
        headers=HEADERS
    )

    assert response.status_code == 404
