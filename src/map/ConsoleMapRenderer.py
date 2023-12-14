from src.data_point import DataPointCollection
from src.map.BaseMapRenderer import BaseMapRenderer


class ConsoleMapRenderer(BaseMapRenderer):
    def __init__(self, console_width, console_height):
        super().__init__()
        self.console_width = console_width
        self.console_height = console_height

    def render(self):
        # Initialize a grid with a border
        grid = [[' ' for _ in range(self.console_width)] for _ in range(self.console_height)]

        # Add data points to the grid
        for data_point in self.data_points:
            lat, lon = data_point.get_latitude(), data_point.get_longitude()
            x, y = self.convert_coordinates_to_console(lat, lon)
            if 0 <= x < self.console_width and 0 <= y < self.console_height:
                grid[y][x] = 'X'  # Mark data points with 'X'

        # Display the grid with a border
        print('+' + '-' * self.console_width + '+')
        for row in grid:
            print('|' + ''.join(row) + '|')
        print('+' + '-' * self.console_width + '+')

    def convert_coordinates_to_console(self, latitude, longitude):
        # Simple conversion assuming latitude and longitude are in the range [-90, 90] and [-180, 180] respectively
        x = int((longitude + 180) / 360 * self.console_width)
        y = int((latitude + 90) / 180 * self.console_height)
        return x, y