import os
import requests
import pytest
from decouple import config


@pytest.fixture(scope='session')
def base_url():
    return 'https://practice.expandtesting.com/notes/api'


# performs the login operation and retrieves the authentication token
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


# fixture to obtain the authorization token for subsequent API requests
@pytest.fixture
def headers(auth_token):
    return {'Authorization': f'Bearer {auth_token}'}


# creates a note and returns its ID for use in specific tests
@pytest.fixture()
def create_note_id(base_url, headers):
    data = {
        "title": "Test Note Title for id",
        "content": "This is a test note content."
    }
    response = requests.post(f'{base_url}/notes', json=data, headers=headers)
    assert response.status_code == 201, f"Failed to create note: {response.text}"
    return response.json().get('id')


# testing POST endpoint
@pytest.mark.smoke
def test_create_note(base_url, headers):
    data = {
        "title": "Test Note Title",
        "content": "This is a test note content."
    }
    response = requests.post(f'{base_url}/notes', json=data, headers=headers)
    assert response.status_code == 201, f"Failed to create note: {response.text}"


# testing GET endpoint
@pytest.mark.smoke
def test_get_all_notes(base_url, headers):
    response = requests.get(f'{base_url}/notes', headers=headers)
    assert response.status_code == 200, f"Failed to fetch all notes: {response.text}"
    notes = response.json()
    assert isinstance(notes, list), "Notes are not returned as a list"


# testing GET endpoint to retreive specific note
@pytest.mark.smoke
def test_get_specific_note(base_url, headers, create_note_id):
    response = requests.get(f'{base_url}/notes/{create_note_id}', headers=headers)
    assert response.status_code == 200, f"Failed to fetch specific note: {response.text}"
    assert response.json().get('id') == create_note_id, "Retrieved note ID doesn't match"


# testing PUT endpoint
@pytest.mark.regression
def test_update_note(base_url, headers, create_note_id):
    data = {
        "title": "Updated Test Note Title",
        "content": "This is an updated test note content."
    }
    response = requests.put(f'{base_url}/notes/{create_note_id}', json=data, headers=headers)
    assert response.status_code == 200, f"Failed to update note: {response.text}"


# testing PATCH endpoint
@pytest.mark.regression
def test_partial_update_note(base_url, headers, create_note_id):
    data = {
        "title": "Updated Test Note Title"
    }
    response = requests.patch(f'{base_url}/notes/{create_note_id}', json=data, headers=headers)
    assert response.status_code == 200, f"Failed to partially update note: {response.text}"


# testing DELETE endpoint
@pytest.mark.regression
def test_delete_note(base_url, headers, create_note_id):
    response = requests.delete(f'{base_url}/notes/{create_note_id}', headers=headers)
    assert response.status_code == 204, f"Failed to delete note: {response.text}"
