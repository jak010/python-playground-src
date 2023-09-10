import datetime
import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        body = "server.cpu.utilization 25.5 1350~~~"
        message = rabbitpy.Message(
            channel,
            body,
            {
                "content_type": "text/plain",
                "timestamp": datetime.datetime.now(),
                "message_type": "graphite metric"
            },
        )
        message.publish('chapter2-example', 'server-metric', mandatory=True)
