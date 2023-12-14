from src.notification.NotificationSender import NotificationSender


class EmailNotificationSender(NotificationSender):

    def __init__(self, message, status='new'):
        super().__init__('email', message, status)

    def send(self):
        # Implementation to send email notification
        pass
