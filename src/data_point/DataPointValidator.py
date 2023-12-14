class DataPointValidator(object):
    def validate_priority(self, priority):
        # Assuming priority is an integer between 1 and 10
        if not (isinstance(priority, int) and 1 <= priority <= 10):
            raise ValueError("Priority must be an integer between 1 and 10.")

    def validate_coordinates(self, latitude, longitude):
        # Assuming latitude and longitude are valid ranges
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError(
                "Invalid coordinates. Latitude must be between -90 and 90, and longitude between -180 and 180.")

    def validate_status(self, status):
        # Assuming status is a string with specific values
        valid_statuses = ["pending", "processing", "completed"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}.")
