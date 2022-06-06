import pika

cred = pika.credentials.PlainCredentials('root', 'root')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cred))

channel = connection.channel()

channel.queue_declare(queue='hello')

while True:
    content = input("here: ")

    if content == "stop":
        break

    channel.basic_publish(exchange='', routing_key='hello', body=content)
    print("success")

connection.close()