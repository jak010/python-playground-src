import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:

        for message in rabbitpy.Queue(channel, "test-messages"):
            message.pprint()
            message.ack()
            print(message.body.decode())
            if message.body.decode() == "stop":
                break
