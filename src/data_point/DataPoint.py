import math

from src.notification import NotificationSender


class DataPoint(object):
    def __init__(self, data_id, latitude, longitude, created_at):
        self.__id = data_id
        self.__latitude = latitude
        self.__longitude = longitude
        self.__created_at = created_at
        self.__collection = None

    def get_id(self):
        return self.__id

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude

    def get_created_at(self):
        return self.__created_at

    def get_collection(self):
        return self.__collection

    def convert_coordinates(self, coord_system):
        if coord_system == "cartesian":
            # Simple conversion for illustration
            x = self.__longitude
            y = self.__latitude
            return x, y
        elif coord_system == "polar":
            # Another simple conversion for illustration
            r = (self.__latitude ** 2 + self.__longitude ** 2) ** 0.5
            theta = math.atan2(self.__latitude, self.__longitude)
            return r, theta
        else:
            raise ValueError("Unsupported coordinate system")

    def get_details(self):
        return {
            'id': self.__id,
            'latitude': self.__latitude,
            'longitude': self.__longitude,
            'created_at': self.__created_at
        }

    def create(self, attributes: list):
        # Check if the number of attributes provided is correct
        if len(attributes) != 4:
            raise ValueError("Incorrect number of attributes provided. Expected 4.")

        # Unpack attributes and create a new DataPoint
        data_id, latitude, longitude, created_at = attributes
        return DataPoint(data_id, latitude, longitude, created_at)

    def set_id(self, data_id):
        self.__id = data_id

    def set_latitude(self, latitude):
        self.__latitude = latitude

    def set_longitude(self, longitude):
        self.__longitude = longitude

    def set_created_at(self, created_at):
        self.__created_at = created_at

    def set_collection(self, collection):
        self.__collection = collection

    def trigger_notification(self, sender: NotificationSender):
        # Implementation to trigger a notification using the provided sender
        pass
