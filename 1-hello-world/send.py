#!/usr/bin/env python
import pika

'''send a single message to the queue'''

# establish a connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# create a hello queue to which the message will be delivered
channel.queue_declare(queue='hello')
# in RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()