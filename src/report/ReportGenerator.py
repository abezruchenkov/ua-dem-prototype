class ReportGenerator(object):
    def __init__(self, message, timestamp, frequency):
        self.___message = message
        self.___timestamp = timestamp
        self.___frequency = frequency
        self.sent = False

    def generate(self):
        pass

    def display_report(self):
        # Implementation to display the report
        pass

    def send_report(self):
        # Implementation to send the report
        self.sent = True

    def mark_as_sent(self):
        # Implementation to mark the report as sent
        pass