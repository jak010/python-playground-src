import pika

# RabbitMQ 서버에 연결합니다.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Exchange를 선언합니다. Type을 'headers'로 설정합니다.
channel.exchange_declare(exchange='amq.headers', exchange_type='headers', durable=True)

# 메시지를 Publish 합니다.
channel.basic_publish(
    exchange='amq.headers',  # 메시지를 전달할 Exchange
    routing_key='',  # Routing Key는 사용하지 않습니다.
    body=b"Hello, Header Exchange!",  # 전송할 메시지 내용
    properties=pika.BasicProperties(
        headers={
            'name': 'a',
        }  # 메시지에 추가할 헤더 속성 설정
    )
)

print(f" [x] Sent '' with headers: ")

# 연결을 닫습니다.
connection.close()
