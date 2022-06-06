import pika, sys, os, json

def main():
    cred = pika.credentials.PlainCredentials('root', 'root')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=cred))
    channel = connection.channel()

    channel.exchange_declare(exchange='test', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='test', queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r" % json.loads(body))

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)