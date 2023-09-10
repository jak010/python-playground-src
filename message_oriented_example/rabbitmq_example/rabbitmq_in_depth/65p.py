import rabbitpy
import time

url = "amqp://guest:guest@localhost:5672/"

connection = rabbitpy.Connection(url)
channel = connection.channel()
queue = rabbitpy.Queue(channel, "example")

print(len(queue))

while len(queue) > 0:
    message = queue.get()
    print("Message:")
    print("ID: %s", message.properties['message_id'])
    print("Time: %s", message.properties['timestamp'].isoformat())
    print("Body: %s", message.body)
    message.ack()
