import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        rabbitpy.Exchange(channel, "reject-messages").declare()
        queue = rabbitpy.Queue(channel, "dlx-example",
                               dead_letter_exchange="rejected-messages")
        queue.declare()
