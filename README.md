# Custom Filtering Library

This library provides simple yet powerful filtering capabilities for data structures in Python.

## Features
- Filter by equality of a property
- Filter by a range of values for a property
- Filter by a substring search in a string property

## Installation
To install the library locally, navigate to the directory where the `setup.py` file is located and run:

## Usage
Here’s a basic example of how to use the filtering library:

```python
from filtering_lib.filters import FilterLibrary

data = [
    {"name": "Alice", "age": 25, "location": "New York"},
    {"name": "Bob", "age": 30, "location": "San Francisco"},
    {"name": "Charlie", "age": 35, "location": "New York"}
]

# Filtering example
filtered_data = FilterLibrary(data).filter_by_equality("location", "New York").get_results()
print(filtered_data)
