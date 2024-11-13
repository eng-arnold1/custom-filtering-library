# examples/example_usage.py
from filtering_lib.filters import FilterLibrary

data = [
    {"name": "Alice", "age": 25, "location": "New York"},
    {"name": "Bob", "age": 30, "location": "San Francisco"},
    {"name": "Charlie", "age": 35, "location": "New York"}
]

# Filtering example
filtered_data = FilterLibrary(data).filter_by_equality("location", "New York").get_results()
print("Filtered by location:", filtered_data)

filtered_data = FilterLibrary(data).filter_by_range("age", 25, 30).get_results()
print("Filtered by age range:", filtered_data)

filtered_data = FilterLibrary(data).filter_by_search("name", "bo").get_results()
print("Filtered by name search:", filtered_data)
