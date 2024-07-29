# RabbitMQ tutorial - "Hello world!"
## Development
```sh
# create virtual environment
python3 -m venv venv
# activate virtual environment
source venv/bin/activate
```
## Useful commands
```sh
# update requirements.txt
pip freeze > requirements.txt
```

Now we can try out our programs in a terminal. First, let's start a consumer, which will run continuously waiting for deliveries:

```sh
python receive.py
# => [*] Waiting for messages. To exit press CTRL+C
```

Now start the producer in a new terminal. The producer program will stop after every run:

```sh
python send.py
# => [x] Sent 'Hello World!'
```

The consumer will print the message:

```sh
# => [*] Waiting for messages. To exit press CTRL+C
# => [x] Received 'Hello World!'
```

Hurray! We were able to send our first message through RabbitMQ. As you might have noticed, the receive.py program doesn't exit. It will stay ready to receive further messages, and may be interrupted with Ctrl-C.

Try to run send.py again in a new terminal.

## References
- https://www.rabbitmq.com/tutorials/tutorial-one-python