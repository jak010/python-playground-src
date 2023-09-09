import pika
import time


def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    # ACK를 지연시킴 (예: 10초)
    time.sleep(10)
    # ACK 보내기
    ch.basic_ack(delivery_tag=method.delivery_tag)


# RabbitMQ 서버에 연결
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 메시지 처리를 위해 callback 함수 등록
channel.basic_consume(queue='SAMPLE_QUEUE', on_message_callback=callback)

print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
