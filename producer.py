import pika, json, sys, os, csv

def convert_to_dict(_id, name, age: int):
    message = {"_id": _id, 
                "name": name,
                "age": age}
    return message

def publish(channel, body, message):

    channel.basic_publish(exchange='test',
                        routing_key='',
                        body=body,
                        properties=pika.BasicProperties(
                            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                        ))

    print(" [x] Sent %r \n" % message)

def main():
    cred = pika.credentials.PlainCredentials('root', 'root')

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cred))

    channel = connection.channel()

    channel.exchange_declare(exchange='test', exchange_type='fanout', durable=True)
    # channel.queue_declare(queue='info', durable=True)

    print('To exit press CTRL+C')

    method = None

    while True:
        i = input('press [i] input or [c] csv: ')
        if i == 'i':
            method = True
            break
        elif i == 'c':
            method = False
            break

    while method:
        _id = input("id: ")
        name = input("name: ")
        age = int(input("age: "))
        message = convert_to_dict(_id, name, age)

        publish(channel, json.dumps(message), message)

    while not method:
        i = input('\ninput file name: ')
        with open(i, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                message = convert_to_dict(row[0], row[1], int(row[2]))
                publish(channel, json.dumps(message), message)

    connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)