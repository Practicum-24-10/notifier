from abc import ABC, abstractmethod

from sender.models.models import Notification


class AbstractNotificationDatabaseService(ABC):
    @abstractmethod
    def __init__(self, connection):
        self.connection = connection

    @abstractmethod
    def save_notification_to_db(self, notification: Notification):
        pass

    @abstractmethod
    def get_notification_by_id(self, notification_id, user_id):
        pass
