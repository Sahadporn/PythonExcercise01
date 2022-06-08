import pika, sys, os, json
from pymongo import MongoClient, errors
import redis
import arrow

def main():

    # connect to mongodb
    client = MongoClient(host="mongodb://localhost:27017/", username="root", password="root")
    db = client["nisitInfo"]
    info_coll = db["info"]

    # connect to rabbitmq
    cred = pika.credentials.PlainCredentials('root', 'root')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=cred))
    channel = connection.channel()

    # decleare exchage and queue
    channel.exchange_declare(exchange='test', exchange_type='fanout', durable=True)

    result = channel.queue_declare(queue='queueinfo', durable=True)
    # queue_name = result.method.queue

    channel.queue_bind(exchange='test', queue='queueinfo')

    print(' [*] Waiting for data. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        content = json.loads(body)

        # Testing pymongo transaction
        # with client.start_session() as session:
        #     with session.start_transaction():
        #         print(" [x] %r" % json.loads(body))

        #         res = info_coll.update_one(
        #             {'_id': content['_id']},
        #             {"$set": {'updated_at': str(arrow.utcnow()),
        #                     'name': content['name'],
        #                     'age': int(content['age'])},
        #              "$setOnInsert": {'created_at': str(arrow.utcnow())}
        #             },
        #             upsert = True,
        #             session=session
        #         )
        #         print("Success: %r \n" % res.upserted_id)

        print(" [x] %r" % json.loads(body))

        res = info_coll.update_one(
            {'_id': content['_id']},
            {"$set": {'updated_at': str(arrow.utcnow()),
                    'name': content['name'],
                    'age': int(content['age'])},
             "$setOnInsert": {'created_at': str(arrow.utcnow())}
            },
            upsert = True
        )
        print("Success: %r \n" % res.upserted_id)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue='queueinfo', on_message_callback=callback, auto_ack=False)

    # channel.basic_consume(
        # queue='info', on_message_callback=callback, auto_ack=False)

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