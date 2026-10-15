import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox', durable=True)

def on_received_message(ch, method, properties, body):
    print(f"Received Message: {body}")

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_received_message)

print("Started consuming...")

channel.start_consuming()