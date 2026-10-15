import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox', durable=True)

message = "This is the first message"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"Sent message: {message}")

connection.close()