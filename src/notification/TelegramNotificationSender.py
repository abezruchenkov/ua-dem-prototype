from src.notification.NotificationSender import NotificationSender


class TelegramNotificationSender(NotificationSender):

    def __init__(self, message, status='new'):
        super().__init__('telegram', message, status)

    def send(self):
        # Implementation to send a Telegram notification
        pass
