import time

import pika
import json
import datetime

# SetUp Pika Credential

pika_credential = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    virtual_host="/",
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

connection = pika.BlockingConnection(pika_credential)
channel = connection.channel()
while True:
    print("Sent Message")
    channel.basic_publish(
        exchange="",
        routing_key="SAMPLE_QUEUE",
        body=json.dumps({"name": "jako", "iss": str(datetime.datetime.now())})
    )
    time.sleep(1)

connection.close()
