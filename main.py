import random
from datetime import datetime

from src.data_point.DataPoint import DataPoint
from src.data_point.DataPointCollection import DataPointCollection
from src.data_point.DataPointValidator import DataPointValidator
from src.map.ConsoleMapRenderer import ConsoleMapRenderer
from src.map.MapRenderer import MapRenderer
from src.notification.EmailNotificationSender import EmailNotificationSender
from src.notification.TelegramNotificationSender import TelegramNotificationSender
from src.receiver.MessageReceiver import MessageReceiver
from src.report.PdfReportGenerator import PdfReportGenerator


def example_console_map(console_width=50, console_height=20):
    map_renderer = ConsoleMapRenderer(console_width, console_height)

    # Create data points
    data_point_collection = DataPointCollection()
    for i in range(20):
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        data_point = DataPoint(i + 1, lat, lon, datetime.now())
        data_point_collection.add(data_point)

    # Render the map in the console
    map_renderer.add_datapoints(data_point_collection.get_collection())
    map_renderer.render()


def example():
    # Instantiate objects
    email_notifier = EmailNotificationSender('Email notification text')
    telegram_notifier = TelegramNotificationSender('Telegram notification text')

    map_renderer = MapRenderer()
    report_generator = PdfReportGenerator("Sample Report", datetime.now(), "daily")

    data_point_validator = DataPointValidator()

    # Create data points
    data_point1 = DataPoint(1, 37.7749, -122.4194, datetime.now())
    data_point2 = DataPoint(2, 34.0522, -118.2437, datetime.now())

    # Add data points to the collection
    data_point_collection = DataPointCollection()
    data_point_collection.add(data_point1)
    data_point_collection.add(data_point2)

    # Trigger notification for data points
    data_point1.trigger_notification(email_notifier)
    data_point2.trigger_notification(telegram_notifier)

    # Receive and validate a message
    message_receiver = MessageReceiver()
    received_message = message_receiver.receive()
    validation_result = message_receiver.validate(data_point_validator)

    # Display the map and render the report
    map_renderer.add_datapoints(data_point_collection.get_collection())
    map_renderer.render()

    report_generator.display_report()
    report_generator.send_report()
    report_generator.mark_as_sent()


if __name__ == '__main__':
    example_console_map(50, 20)
    # example()
