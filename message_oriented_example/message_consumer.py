import pika

pika_credential = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    virtual_host="/",
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

connection = pika.BlockingConnection(pika_credential)


def callback(ch, method, properties, body):
    print(f"Received message: {body}")


channel = connection.channel()

# 큐에서 메시지 받기
channel.basic_consume(queue='SAMPLE_QUEUE', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
