import pika

# RabbitMQ 서버에 연결
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

exchange_name = 'amq.direct'
channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

while True:
    import time
    print(f"[DIRECT] Message Publisher")
    channel.basic_publish(exchange=exchange_name, routing_key="SAMPLE_QUEUE", body='Direct Message')

connection.close()
