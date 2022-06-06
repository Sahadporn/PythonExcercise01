import sys
import pika

cred = pika.credentials.PlainCredentials('root', 'root')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cred))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# channel.queue_bind(exchange='logs', queue=result.method.queue)

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "info: Hello World!"
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message,
                     )
print(" [x] Sent %r:%r" % (severity, message))
connection.close()