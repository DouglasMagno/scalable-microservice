import pytest
from unittest.mock import MagicMock, patch
from app.services import DataService

@pytest.fixture
def mock_collection():
    return MagicMock()

@pytest.fixture
def data_service(mock_collection):
    mock_db_client = MagicMock()
    mock_db_client.get_collection.return_value = mock_collection
    service = DataService(mock_db_client)
    return service

def test_create_data_should_return_inserted_id(data_service, mock_collection):
    # Arrange
    test_item = {"field1": "Test Data", "field2": 123}
    expected_id = "test_id"
    mock_insert_result = MagicMock()
    mock_insert_result.inserted_id = expected_id
    mock_collection.insert_one.return_value = mock_insert_result

    # Act
    result = data_service.create_data(test_item)

    # Assert
    assert result == {"id": expected_id}
    mock_collection.insert_one.assert_called_once_with(test_item)

def test_create_data_with_database_error_should_raise_exception(data_service, mock_collection):
    # Arrange
    test_item = {"field1": "Test Data", "field2": 123}
    mock_collection.insert_one.side_effect = Exception("Database error")

    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        data_service.create_data(test_item)
    assert "Database error" in str(exc_info.value)
    mock_collection.insert_one.assert_called_once_with(test_item)

def test_get_all_data_should_return_list_of_documents(data_service, mock_collection):
    # Arrange
    mock_documents = [
        {"_id": "id1", "field1": "Data1", "field2": 100},
        {"_id": "id2", "field1": "Data2", "field2": 200},
    ]
    # Mock the cursor to return the documents
    mock_cursor = mock_collection.find.return_value
    mock_cursor.__iter__.return_value = mock_documents

    # Act
    result = data_service.get_all_data()

    # Assert
    assert result == mock_documents
    mock_collection.find.assert_called_once()

def test_get_all_data_should_return_empty_list_when_no_documents(data_service, mock_collection):
    # Arrange
    mock_documents = []
    mock_cursor = mock_collection.find.return_value
    mock_cursor.__iter__.return_value = mock_documents

    # Act
    result = data_service.get_all_data()

    # Assert
    assert result == []
    mock_collection.find.assert_called_once()

def test_get_all_data_with_database_error_should_raise_exception(data_service, mock_collection):
    # Arrange
    mock_collection.find.side_effect = Exception("Database error")

    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        data_service.get_all_data()
    assert "Database error" in str(exc_info.value)
    mock_collection.find.assert_called_once()
