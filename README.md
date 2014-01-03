servicebus.py
=============

inspired from https://github.com/mateodelnorte/servicebus - python version



TODO:

- add a registry for Qs and pubsubQs -> bus/bus.py maintains a list of Qs
- add RPC feature
- unit test the bus
- handle connection failure: https://pika.readthedocs.org/en/latest/modules/channel.html
- in case of error send/publish on event.error: https://pika.readthedocs.org/en/latest/examples/blocking_publish_mandatory.html
- allow middleware to be plugged-in
