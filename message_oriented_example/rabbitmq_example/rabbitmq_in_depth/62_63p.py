import rabbitpy
import time

url = "amqp://guest:guest@localhost:5672/"

connection = rabbitpy.Connection(url)

# 커넥션에 새로운 채널 열기
channel = connection.channel()
channel.enable_publisher_confirms()

# 채널을 인자로 전달해서 새로운 익스체인지 객체 생성
exchange = rabbitpy.Exchange(channel, "chapter2-example")
exchange.declare()

# 채널을 전달해 새로운 Queue 객체 생겅하기
queue = rabbitpy.Queue(channel, "example")
result = queue.declare()
print(result)

# RabbitMQ 서버의 Queue와 Exchange 연결하기
queue.bind(exchange, "example-routing-key")

for message_number in range(1, 11):
    time.sleep(1)
    print("Test Message %i" % message_number)
    _message = rabbitpy.Message(
        channel,
        "Test Message %i" % message_number,
        {"content_type": "text/plain"}, opinionated=True

    )
    _message.publish(exchange, "example-routing-key")
