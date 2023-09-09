import pika


def check_for_messages():
    # RabbitMQ 서버에 연결
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # 큐 이름 설정
    queue_name = 'SAMPLE_QUEUE'

    # 메시지 받기
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)
    if method_frame:
        print(f"Received durable message: {body}")
    else:
        print("No durable message received.")

    connection.close()


# 메시지 확인 함수 실행
check_for_messages()
