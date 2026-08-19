from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, to:str, whom:str, body:str):
        pass

class EmailNotificationService(NotificationService):
    def send(self, to:str, whom:str, body:str):
        print(f"Sending an Email -")
        print(f"From: {whom}")
        print(f"To: {to}")
        print(f"Body: {body}")


class SendEmailGrid:
    def send_email(self, recipient:str, subject:str, content:str):
        print(f"Sending an EmailGrid -")
        print(f"From: {recipient}")
        print(f"To: {subject}")
        print(f"Body: {content}")

class SendEmailAdapter(NotificationService):
    def __init__(self, email_gird_service: SendEmailGrid):
        self.__email_grid_service = email_gird_service

    def send(self, to:str, whom:str, body:str):
        self.__email_grid_service.send_email(to, whom, body)

class OrderService:
    def __init__(self, email_notification_service: NotificationService):
        self.__email_notification_service = email_notification_service

    def create_order(self):
        self.__email_notification_service.send("amaankhxn2000@gmail.com", "Amaan", "It's done bro")

object_email_service = SendEmailGrid()
object_email_adapter = SendEmailAdapter(object_email_service)
object_order_service = OrderService(object_email_adapter)
object_order_service.create_order()


        





