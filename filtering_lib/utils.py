# filtering_lib/utils.py
def validate_property_exists(data, property):
    """Check if a property exists in the dataset."""
    if not all(property in item for item in data):
        raise ValueError(f"The property '{property}' does not exist in all items of the dataset.")
