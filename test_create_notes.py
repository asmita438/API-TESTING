
import requests
import pytest
from decouple import config


@pytest.fixture(scope='session')
def base_url():
    return 'https://practice.expandtesting.com/notes/api'


@pytest.fixture(scope='session')
def auth_token():
    login_url = 'https://practice.expandtesting.com/notes/api/users/login'
    login_data = {
        "email": config('USERNAME'),
        "password": config('PASSWORD')
    }
    response = requests.post(login_url, json=login_data)
    assert response.status_code == 200, f"Failed to authenticate: {response.text}"
    return response.json().get('token')


@pytest.fixture
def headers(auth_token):
    return {'Authorization': f'Bearer {auth_token}'}


# pass multiple datasets to create notes
@pytest.fixture(params=[
    {"title": "First Note Title test", "content": "This is the first note."},
    {"title": "Second Note Title test", "content": "This is the second note."},
    {"title": "Third Note Title test", "content": "This is content for the third note."}
])
def note_data(request):
    return request.param


@pytest.mark.smoke
def test_create_note(base_url, headers, note_data):
    response = requests.post(f'{base_url}/notes', json=note_data, headers=headers)
    assert response.status_code == 201, f"Failed to create note: {response.text}"
    created_note_id = response.json().get('id')
    assert created_note_id is not None, "Note ID not found in response"


# pass multiple datasets for partial update
@pytest.mark.parametrize("update_data", [
    {"title": "Updated First Note Title", "content": "Updated content for the first note."},
    {"title": "Updated Second Note Title", "content": "Updated content for the second note."},
    {"title": "Updated Third Note Title", "content": "Updated content for the third note."}
])
@pytest.mark.regression
def test_partial_update_note(base_url, headers, note_data, update_data):
    response = requests.patch(f'{base_url}/notes/{note_data["title"]}', json=update_data, headers=headers)
    assert response.status_code == 200, f"Failed to partially update note: {response.text}"
