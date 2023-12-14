# Ua Demining Project (Model Prototype)

## Description

This project serves as a model prototype for the upcoming Ua Demining main project. The prototype provides an initial demonstration of key functionalities and serves as a foundation for further development.

## Table of Contents

- [Usage](#usage)
- [Examples](#examples)
- [Example Output](#example-output)
- [Team](#team)

## Usage 

```python
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

report_generator.generate()
report_generator.send_report()
report_generator.mark_as_sent()
```

## Examples
```python
console_width = 50
console_height = 20

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
```

## Example Output
```
+--------------------------------------------------+
|                                  X               |
|                                     X            |
|                                                  |
|                                                  |
|                           XX                X    |
|                  X         X                     |
|                                                  |
|                                                  |
|   X                                   X          |
|                                            X     |
|                                                  |
|                                                  |
|                           X                      |
|                                  X      X        |
|    X      X                                      |
|                                     X   X        |
|                                                  |
|                     X   X                        |
|   X                                              |
|                                                  |
+--------------------------------------------------+
```

## Team
- Anna Shliapkina
- Dmytro Lytvynenko
- Oleksii Bezruchenkov

