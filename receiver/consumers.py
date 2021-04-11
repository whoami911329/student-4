import json
from channels.generic.websocket import WebsocketConsumer


class ReceiverConsumer(WebsocketConsumer):
    """
    Here consumer receive the messages from the response
    """

    def connect(self):
        pass

    def disconnect(self, close_code):
        pass

    def receive(self):
        pass
