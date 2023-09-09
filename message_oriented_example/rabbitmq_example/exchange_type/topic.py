import pika
from pika.exchange_type import ExchangeType

# RabbitMQ 서버에 연결
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# Exchange 설정 (exchange_type='topic')
exchange_name = 'amq.topic'

channel.exchange_declare(exchange=exchange_name, exchange_type=ExchangeType.topic, durable=True)

# 메시지 보내기 (exchange와 routing_key 설정)

routing_key = 'a.b'  # 라우팅 키 설정

channel.basic_publish(
    exchange=exchange_name,
    routing_key=routing_key,
    body=b'Topic Message',
)

print(f"Sent '' with routing key '{routing_key}' to '{exchange_name}'")

connection.close()
