import rabbitpy

consume = rabbitpy.consume('amqp://guest:guest@localhost:5672/%2F', "test-messages")

for message in consume:
    message.pprint()
    message.ack()
