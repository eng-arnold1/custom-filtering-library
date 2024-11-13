# Custom Filtering Library

This is a Python library that provides customizable filtering functionality for data. It supports filtering by equality, range, and search within a collection of dictionaries.

This library provides simple yet powerful filtering capabilities for data structures in Python.

## Features of the library

-Filter by Equality: Filter data based on exact matches for specified fields.
-Filter by Range: Filter data based on a specified range for numeric fields.
-Filter by Search: Search for data based on partial string matches.

## Installation Steps

## Requirements

Before using the library, make sure to have Python 3.6+ installed. 
## Note

It is recommended to use a virtual environment to manage dependencies.

## Dependencies
Python 3.6 or higher
pytest: For running tests.
setuptools: For packaging the library.
You can install the required dependencies by running the following command:

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
```



## Things To Note 
Before using the library, make sure to have Python 3.6+ installed. It is recommended to use a virtual environment to manage dependencies.

## Dependencies
Python 3.6 or higher
pytest: For running tests.
setuptools: For packaging the library.
You can install the required dependencies by running the following command:

pip install -e

## Installation from my Github account

Clone the repository to your local machine:

git clone https://github.com/yourusername/custom_filtering_library.git
cd custom_filtering_library
Set up a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate  # For Linux or macOS
venv\Scripts\activate     # For Windows
Install the library in editable mode:

pip install -e .
## Running Tests
To run the tests for the library, use pytest:

pytest tests/test_filters.py
All tests should pass if everything is working correctly.

Example Usage
Filter by Equality
from filtering_lib.filters import FilterLibrary

data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
filter_obj = FilterLibrary(data)
result = filter_obj.filter_by_equality("name", "Alice").get_results()

print(result)  # Output: [{"name": "Alice", "age": 25}]
Filter by Range
data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]
filter_obj = FilterLibrary(data)
result = filter_obj.filter_by_range("age", 28, 36).get_results()

print(result)  # Output: [{"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]
Filter by Search
data = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
filter_obj = FilterLibrary(data)
result = filter_obj.filter_by_search("name", "li").get_results()

print(result)  # Output: [{"name": "Alice"}, {"name": "Charlie"}]

Feel free to fork the repository, submit issues, or contribute improvements via pull requests. Contributions are welcome!

