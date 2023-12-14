from src.data_point import DataPointValidator


class MessageReceiver(object):
    def receive(self):
        # Implementation to receive a message
        pass

    def get_message(self):
        # Implementation to get the received message
        pass

    def validate(self, validator: DataPointValidator):
        # Implementation to validate a data point using the provided validator
        pass