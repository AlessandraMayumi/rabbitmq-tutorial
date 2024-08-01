# RabbitMQ tutorial - Routing

Our logging system from the previous tutorial broadcasts all messages to all consumers. We want to extend that to allow filtering messages based on their severity. For example we may want the script which is writing log messages to the disk to only receive critical errors, and not waste disk space on warning or info log messages.

```sh
# shell 1
python receive_logs_direct.py warning error > logs_from_rabbit.log

# shell 2
python receive_logs_direct.py info warning error

# shell 3
python emit_log_direct.py error "Run. Run. Or it will explode."
```

## References
- https://www.rabbitmq.com/tutorials/tutorial-four-python
