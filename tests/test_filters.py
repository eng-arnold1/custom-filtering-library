# tests/test_filters.py
import pytest
from filtering_lib.filters import FilterLibrary

@pytest.fixture
def sample_data():
    return [
        {"name": "Alice", "age": 25, "location": "New York"},
        {"name": "Bob", "age": 30, "location": "San Francisco"},
        {"name": "Charlie", "age": 35, "location": "New York"}
    ]

def test_filter_by_equality(sample_data):
    lib = FilterLibrary(sample_data)
    result = lib.filter_by_equality("location", "New York").get_results()
    assert len(result) == 2

def test_filter_by_range(sample_data):
    lib = FilterLibrary(sample_data)
    result = lib.filter_by_range("age", 26, 35).get_results()
    assert len(result) == 2

def test_filter_by_search(sample_data):
    lib = FilterLibrary(sample_data)
    result = lib.filter_by_search("name", "Alice").get_results()
    assert len(result) == 1
