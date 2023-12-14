from src.data_point import DataPoint


class DataPointCollection(object):
    def __init__(self):
        self.__points = []

    def add(self, data_point: DataPoint):
        self.__points.append(data_point)

    def delete(self, data_point: DataPoint):
        self.__points.remove(data_point)

    def filter_collection(self, condition_function):
        # Implementation to filter the collection based on a condition
        filtered_points = [point for point in self.__points if condition_function(point)]
        return filtered_points

    def sort_collection(self, key_function=None, reverse=False):
        # Implementation to sort the collection based on a key function
        self.__points.sort(key=key_function, reverse=reverse)

    def get_collection(self):
        return self.__points
