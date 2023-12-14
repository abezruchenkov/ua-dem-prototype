from src.data_point import DataPointCollection


class BaseMapRenderer(object):
    def __init__(self):
        self.data_points = []

    def add_datapoints(self, collection: DataPointCollection):
        self.data_points.extend(collection)

    def render(self):
        # Implementation to render the map with data points
        raise NotImplemented
