import pika, sys, os, json
from pymongo import MongoClient, errors
import redis
import arrow

def main():

    # connect to mongodb
    client = MongoClient(host="mongodb://localhost:27017/", username="root", password="root")
    db = client["nisitInfo"]
    info_coll = db["info"]

    # connect to redis
    # redis_client = redis.StrictRedis(host='localhost', port=6379, password='root')

    # connect to rabbitmq
    cred = pika.credentials.PlainCredentials('root', 'root')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=cred))
    channel = connection.channel()

    # decleare exchage and queue
    channel.exchange_declare(exchange='test', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='test', queue=queue_name)

    print(' [*] Waiting for data. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        content = json.loads(body)
        print(" [x] %r" % json.loads(body))
        
        res = info_coll.update(
            {'_id': content['_id']},
            {"$set": {'updated_at': arrow.utcnow(),
                    'name': content['name'],
                    'age': int(content['age'])}
            },
            upsert = True
        )

        # check id from redis
        # if redis_client.get(content['_id']) == None:
            
        #     # get utc date and merge to existing content
        #     date = {
        #         'created_at': str(arrow.utcnow()),
        #         'updated_at': str(arrow.utcnow())
        #     }

        #     merged = {**content, **date}

        #     # save new data to redis and mongodb
        #     redis_client.set(merged['_id'], merged['created_at'])
        #     res = info_coll.insert_one(merged)

        #     print("Save Success: ", res.inserted_id)

        # else:
        #     res = info_coll.update_one({'_id': content['_id']}, {'$set': {
        #         'updated_at': str(arrow.utcnow()),
        #         'name': content['name'],
        #         'age': int(content['age'])
        #         }})
                
        #     print("Update Success: ", res)

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