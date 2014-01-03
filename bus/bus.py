import logging
import pika
import json


class Bus(object):

    def __init__(self, url=""):
        if not url:
            url = "amqp://guest:guest@localhost:5672/%2F"
        self._channel = self.__connect(url)

    def send(self, event, message):
        self._channel.queue_declare(queue=event, durable=False, auto_delete=True)
        self._channel.basic_publish(exchange='', routing_key=event, body=message,
                                    properties=pika.BasicProperties(content_type='application/json', delivery_mode=2))

    def listen(self, event, callback):
        self._channel.queue_declare(queue=event, durable=False, auto_delete=True)
        self._channel.basic_consume(callback, queue=event, no_ack=True)
        self._channel.start_consuming()

    def publish(self, event, message):
        self._channel.exchange_declare(exchange='amq.topic', type='topic', durable=True)
        self._channel.basic_publish(exchange='amq.topic', routing_key=event, body=json.dumps(message),
                                    properties=pika.BasicProperties(content_type='application/json', delivery_mode=2))

    def subscribe(self, event, callback):
        self._channel.exchange_declare(exchange='amq.topic', type='topic', durable=True)
        result = self._channel.queue_declare(durable=False, auto_delete=True)
        queue_name = result.method.queue
        self._channel.queue_bind(exchange='amq.topic', queue=queue_name, routing_key=event)
        self._channel.basic_consume(callback, queue=queue_name, no_ack=True)
        self._channel.start_consuming()

    def __connect(self, url):
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        logging.info("rabbit connected to %s" % url)
        return channel