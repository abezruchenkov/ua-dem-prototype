class NotificationSender(object):
    def __init__(self, notification_type, message, status='new'):
        self.__notificationType = notification_type
        self.__message = message
        self.__status = status

    def send(self):
        raise NotImplemented
