import pika

# RabbitMQ 서버에 연결
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 큐 이름 설정
queue_name = 'SAMPLE_QUEUE'

# 메시지 보내기 (내구성 메시지)
channel.basic_publish(
    exchange='',
    routing_key=queue_name,
    body='Durable Message',
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # 메시지 속성 설정 (delivery_mode=2로 내구성 설정)
    )
)

print("Sent 'Durable Message' to my_queue with durability")

connection.close()
