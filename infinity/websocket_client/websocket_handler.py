import threading


class WebsocketHandler:
    def __init__(self):
        self.ws_id = None
        self.client = None
        self.request_id = 1
        self.reconnect_count = 0
        self.subscribed_channels = []
        self.reconnect_lock = threading.Lock()
        self.is_open = False
        self.force_reconnect_event = None
        self.last_reconnect_timestamp = None