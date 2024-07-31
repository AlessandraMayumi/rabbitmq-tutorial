# RabbitMQ tutorial - Publish/Subscribe

In this part we'll do something completely different -- we'll deliver a message to multiple consumers. This pattern is known as "publish/subscribe".

The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all.

```sh
# to save logs to a file
python receive_logs.py > logs_from_rabbit.log

# to see the logs on your screen
python receive_logs.py

# to emit logs
python emit_log.py
```




## References
- https://www.rabbitmq.com/tutorials/tutorial-three-python