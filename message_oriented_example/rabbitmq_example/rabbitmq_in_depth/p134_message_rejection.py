import rabbitpy

r = rabbitpy.consume("amqp://guest:guest@localhost:5672/%2f", "test-messages")

for message in r:
    print("Redelivered: %s", message.redelivered)
    message.reject(True)
