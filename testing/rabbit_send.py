import pika, arrow, json

cred = pika.credentials.PlainCredentials('root', 'root')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=cred))

channel = connection.channel()

channel.exchange_declare(exchange='test', exchange_type='fanout')

message = {"_id": "00000000001", 
        "name": "Carrot Cake",
        "age": 27, 
        "created_at": str(arrow.utcnow()),
        "updated_at": str(arrow.utcnow())}

# while True:
#         _id = input("id: ")
#         name = input("name: ")
#         age = int(input("age: "))

#         if _id == KeyboardInterrupt: break

#         message = {"_id": _id, 
#                 "name": name,
#                 "age": age, 
#                 "created_at": str(arrow.utcnow()),
#                 "updated_at": str(arrow.utcnow())}

convert_to_json = json.dumps(message)

channel.basic_publish(exchange='test',
                      routing_key='',
                      body=convert_to_json,
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))
print(" [x] Sent %r" % message)
connection.close()