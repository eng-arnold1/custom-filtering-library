# filtering_lib/filters.py
class FilterLibrary:
    def __init__(self, data):
        self.data = data

    def filter_by_equality(self, property, value):
        """Filter items where a specific property equals a given value."""
        self.data = [item for item in self.data if item.get(property) == value]
        return self

    def filter_by_range(self, property, min_value, max_value):
        """Filter items where a property is within a specified range."""
        self.data = [item for item in self.data if min_value <= item.get(property, float('-inf')) <= max_value]
        return self

    def filter_by_search(self, property, search_string):
        """Filter items where a string property contains a substring."""
        self.data = [item for item in self.data if search_string.lower() in str(item.get(property, "")).lower()]
        return self

    def get_results(self):
        """Return the filtered data."""
        return self.data
