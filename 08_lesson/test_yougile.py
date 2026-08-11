import requests

BASE_URL = 'https://ru.yougile.com/api-v2/'
API_TOKEN = "ВВедите сюда токен из сообщения"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
    }

test_project_data = {
    "title": "Мой первый проект из автотеста"
    }
test_project_data2 = {
    "title": "Мой второй проект из автотеста"
    }
test_project_data3 = {
    "title": "Мой третий проект из автотеста"
    }
test_project_none = {
    "title": ""
}
test_project_new_name = {
    "title": "Мой проект из автотеста с новым названием"
}
new_title = "Мой проект с новым названием"


def test_create_project_positive():
    response = requests.post(
        f"{BASE_URL}/projects",
        json=test_project_data,
        headers=HEADERS
    )

    assert response.status_code == 201
    project_id = response.json().get('id')

    response = requests.delete(
        f"{BASE_URL}/projects/{project_id}",
        json=test_project_data,
        headers=HEADERS
    )


def test_create_project_negative():
    response = requests.post(
        f"{BASE_URL}/projects",
        json=test_project_none,
        headers=HEADERS
    )

    assert response.status_code == 400


def test_get_project_id_positive():
    response = requests.post(
        f"{BASE_URL}/projects",
        json=test_project_data2,
        headers=HEADERS
    )
    project_id = response.json().get('id')
    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )

    assert response.status_code == 200
    response = requests.delete(
        f"{BASE_URL}/projects/{project_id}",
        json=test_project_data,
        headers=HEADERS
    )


def test_get_project_id_negativ():
    response = requests.get(
        f"{BASE_URL}/projects/21212",
        headers=HEADERS
    )

    assert response.status_code == 404


def test_put_project_id_positive():
    response = requests.post(
        f"{BASE_URL}/projects",
        json=test_project_data3,
        headers=HEADERS
    )
    project_id = response.json().get('id')
    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json={"title": new_title},
        headers=HEADERS
    )
    assert response.status_code == 200, f"Update failed: {response.text}"

    get_response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS
    )
    assert get_response.status_code == 200, f"Get failed: {get_response.text}"

    updated_title = get_response.json().get('title')
    assert updated_title == new_title, f"Expected '{
        new_title}', got '{updated_title}'"

    response = requests.delete(
        f"{BASE_URL}/projects/{project_id}",
        json=test_project_data,
        headers=HEADERS
    )


def test_put_project_id_negative():
    response = requests.put(
        f"{BASE_URL}/projects/1212121212",
        json=test_project_new_name,
        headers=HEADERS
    )

    assert response.status_code == 404
