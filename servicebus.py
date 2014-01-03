from bus.bus import Bus


class ServiceBus(object):

    def __init__(self, url=""):
        self._bus = Bus(url)

    def send(self, event, message):
        self._bus.send(event, message)

    def listen(self, event, callback):
        self._bus.listen(event, callback)

    def publish(self, event, message):
        self._bus.publish(event, message)

    def subscribe(self, event, callback):
        self._bus.subscribe(event, callback)