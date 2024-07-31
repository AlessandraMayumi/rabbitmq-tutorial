# RabbitMQ tutorial - Work Queues

The main idea behind Work Queues (aka: Task Queues) is to avoid doing a resource-intensive task immediately and having to wait for it to complete. Instead we schedule the task to be done later. We encapsulate a task as a message and send it to the queue. A worker process running in the background will pop the tasks and eventually execute the job. When you run many workers the tasks will be shared between them.

This concept is especially useful in web applications where it's impossible to handle a complex task during a short HTTP request window.

### Round-robin dispatching

If we are building up a backlog of work, we can just add more workers and that way, scale easily.

By default, RabbitMQ will send each message to the next consumer, in sequence. On average every consumer will get the same number of messages. This way of distributing messages is called round-robin. 

```sh
# shell 1
python worker.py
# => [*] Waiting for messages. To exit press CTRL+C
```

```sh
# shell 2
python worker.py
# => [*] Waiting for messages. To exit press CTRL+C
```

In the third one we'll publish new tasks. Once you've started the consumers you can publish a few messages:

```sh
# shell 3
python new_task.py First message.
python new_task.py Second message..
python new_task.py Third message...
python new_task.py Fourth message....
python new_task.py Fifth message.....
```
## Development

## References
- https://www.rabbitmq.com/tutorials/tutorial-two-python