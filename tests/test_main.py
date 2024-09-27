from fastapi.testclient import TestClient
from app.main import app, get_server_context
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_service():
    service = MagicMock()
    return service

@pytest.fixture
def test_app(mock_service):
    class MockServerContext:
        def __init__(self):
            self.service = mock_service

    app.dependency_overrides[get_server_context] = lambda: MockServerContext()
    client = TestClient(app)
    yield client
    app.dependency_overrides = {}

def test_create_data_should_return_same_fields_and_values(test_app, mock_service):
    # Arrange
    test_data = {"field1": "Test Data", "field2": 123}
    expected_response = {"id": "test_id"}

    mock_service.create_data.return_value = expected_response

    # Act
    response = test_app.post("/data", json=test_data)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_response
    mock_service.create_data.assert_called_once_with(test_data)

def test_read_data_should_return_data_list(test_app, mock_service):
    # Arrange
    expected_data = [
        {"_id": "test_id_1", "field1": "Data1", "field2": 100},
        {"_id": "test_id_2", "field1": "Data2", "field2": 200},
    ]
    mock_service.get_all_data.return_value = expected_data

    # Act
    response = test_app.get("/data")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_data
    mock_service.get_all_data.assert_called_once()

def test_read_data_should_return_empty_list_when_no_data(test_app, mock_service):
    # Arrange
    expected_data = []
    mock_service.get_all_data.return_value = expected_data

    # Act
    response = test_app.get("/data")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_data
    mock_service.get_all_data.assert_called_once()

def test_read_data_with_large_dataset_should_return_all_data(test_app, mock_service):
    # Arrange
    expected_data = [{"_id": f"id_{i}", "field1": f"Data{i}", "field2": i} for i in range(1000)]
    mock_service.get_all_data.return_value = expected_data

    # Act
    response = test_app.get("/data")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_data
    mock_service.get_all_data.assert_called_once()
