import pika

# RabbitMQ 서버에 연결
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange="amq.fanout", exchange_type='fanout', durable=True)

channel.basic_publish(exchange="amq.fanout", routing_key="", body="Fanout Message")

print("[FANOUT] Message Publisher")

connection.close()
