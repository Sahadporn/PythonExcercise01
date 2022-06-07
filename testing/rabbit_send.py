import pika, arrow, json

cred = pika.credentials.PlainCredentials('root', 'root')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cred))

channel = connection.channel()

channel.exchange_declare(exchange='test', exchange_type='fanout')

# message = {"_id": "00000000001", 
#         "name": "Carrot Cake",
#         "age": 27, 
#         }

# message = {"_id": "00000000002", 
#         "name": "Som Tum",
#         "age": 29
#         }

print('To exit press CTRL+C')

while True:
    try:
        _id = input("id: ")
        name = input("name: ")
        age = int(input("age: "))
        message = {"_id": _id, 
                "name": name,
                "age": age}
    except KeyboardInterrupt:
        break

    convert_to_json = json.dumps(message)

    channel.basic_publish(exchange='test',
                        routing_key='',
                        body=convert_to_json,
                        properties=pika.BasicProperties(
                            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                        ))
    print(" [x] Sent %r" % message)

connection.close()