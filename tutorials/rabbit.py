from amqpstorm import Connection
from amqpstorm import Message
import arrow

connection = Connection('127.0.0.1', 'root', 'root')

# Set a channel to connect
channel = connection.channel()

channel.queue.declare('simple_queue')

content = {
    'content_type': 'text/plain',
    'headers': {
        "_id": "00000000001", 
        "name": "Carrot Cake",
        "age": 27, 
        "created_at": str(arrow.utcnow()),
        "updated_at": str(arrow.utcnow())
    }
}

msg = Message.create(channel=channel, body='get out', properties=content)

msg.publish(routing_key = 'simple_queue')

connection.close()
