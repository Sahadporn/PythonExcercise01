import sys
import pika

cred = pika.credentials.PlainCredentials('root', 'root')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cred))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# channel.queue_bind(exchange='logs', queue=result.method.queue)

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or "info: Hello World!"
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message,
                     )
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()