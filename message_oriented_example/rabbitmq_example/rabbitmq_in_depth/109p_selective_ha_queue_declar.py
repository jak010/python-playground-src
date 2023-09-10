import rabbitpy

connection = rabbitpy.Connection()

try:
    with connection.channel() as channel:
        queue = rabbitpy.Queue(
            channel,
            "my-2nd-ha-queue",
            arguments={"x-ha-policy": 'nodes',
                       "x-ha-nodes": [
                           "rabbit@node1",
                           "rabbit@node2",
                           "rabbit@node3"]
                       })

        if queue.declare():
            print("Queue declared")
except rabbitpy.exceptions.RemoteClosedChannelException as error:
    print("Queue declare failed: %s" % error)
