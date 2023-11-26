# API Smoke Tests Documentation

This document outlines the purpose and validation criteria for the tests performed on the notes API endpoints. The tests are designed to validate the basic functionalities of creating, retrieving, updating, and deleting notes, while also ensuring that the authentication mechanism works as expected.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Test Scenarios](#test-scenarios)


## Installation
- Ensure you shave Python installed
- pip install -r requirements.txt

## Usage
There are two test files in this suite, namely:
- test_notes_api.py
- test_create_notes.py

To run specific test files, go to the project directory and use following commands:
* pytest <test_file_name>.py

To run smoke or regression tests within those test files use following commands:
* pytest <test_file_name>.py -m smoke
* pytest <test_file_name>.py -m regression

## Configuration
In the credentials.env file, replace 'USERNAME' and 'PASSWORD' variables with appropriate login credentials.

## Test Scenarios
### Create Note (POST)
- **Purpose:** Validates the ability to create a new note via a POST request to the specified API endpoint.
- **Validation Criteria:**
    - Verifies that a note can be successfully created with different sets of data.
    - Checks that the API responds with a status code of 201 (Created) upon successful note creation.
    - Validates the presence of the 'id' attribute in the response, confirming the note's creation.
    - Uses parameterization to test with multiple datasets for note creation.


### Get Note (GET)
- **Purpose:** Validates the ability to display a note using a GET request to the specified API endpoint.
- **Validation Criteria:**
    - Verifies that all notes are fetched .
    - Ensures that the API responds with a status code of 200 (OK) upon successful update.
    - Validates the updated note's title and content using parameterization with different datasets.

### Update Note (PATCH)
- **Purpose:** Validates the ability to partially update a note using a PATCH request to the specified API endpoint.
- **Validation Criteria:**
    - Verifies that a note can be updated with new data while preserving existing information.
    - Ensures that the API responds with a status code of 200 (OK) upon successful update.
    - Validates the updated note's title and content using parameterization with different datasets.

### Delete Note (DELETE)
- **Purpose:** Validates the ability to delete a note using a DELETE request to the specified API endpoint.
- **Validation Criteria:**
    - Verifies that a note can be successfully deleted.
    - Checks that the API responds with a status code of 204 (No Content) upon successful deletion.
    - Ensures that the deleted note is no longer retrievable from the system.



