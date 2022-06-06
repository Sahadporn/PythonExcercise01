import sys
import pika

cred = pika.credentials.PlainCredentials('root', 'root')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cred))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# channel.queue_bind(exchange='logs', queue=result.method.queue)

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message,
                     )
print(" [x] Sent %r" % message)
connection.close()