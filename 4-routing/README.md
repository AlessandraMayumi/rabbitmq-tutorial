# RabbitMQ tutorial - Routing

Our logging system from the previous tutorial broadcasts all messages to all consumers. We want to extend that to allow filtering messages based on their severity.

Subscribe only to a subset of the messages to the log file (to save disk space), while still being able to print all of the log messages on the console.

```sh
# shell 1 messages to the log file
python receive_logs_direct.py warning error > logs_from_rabbit.log

# shell 2 log messages on the console
python receive_logs_direct.py info warning error

# shell 3 severity message
python emit_log_direct.py error "Run. Run. Or it will explode."
python emit_log_direct.py info "Just a general info."
python emit_log_direct.py warning "Is it smoke?"
```

## References
- https://www.rabbitmq.com/tutorials/tutorial-four-python
