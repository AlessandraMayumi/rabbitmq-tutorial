# RabbitMQ tutorial - Topic

We're going to use a `topic` exchange in our logging system. The routing keys of logs will have two words: "<facility>.<severity>".

\* (star) can substitute for exactly one word.

\# (hash) can substitute for zero or more words.

```sh
# To receive all the logs run:
python receive_logs_topic.py "#"

# To receive all logs from the facility "kern":
python receive_logs_topic.py "kern.*"

# Or if you want to hear only about "critical" logs:
python receive_logs_topic.py "*.critical"

# You can create multiple bindings:
python receive_logs_topic.py "kern.*" "*.critical"

# And to emit a log with a routing key "kern.critical" type:
python emit_log_topic.py "kern.critical" "A critical kernel error"
```

## References
- https://www.rabbitmq.com/tutorials/tutorial-five-python
