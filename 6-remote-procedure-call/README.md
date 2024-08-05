# RabbitMQ tutorial - Remote procedure call (RPC)

### A note on RPC
Although RPC is a pretty common pattern in computing, it's often criticised. The problems arise when a programmer is not aware whether a function call is local or if it's a slow RPC. Confusions like that result in an unpredictable system and adds unnecessary complexity to debugging. Instead of simplifying software, misused RPC can result in unmaintainable spaghetti code.

Bearing that in mind, consider the following advice:

Make sure it's obvious which function call is local and which is remote.
Document your system. Make the dependencies between components clear.
Handle error cases. How should the client react when the RPC server is down for a long time?
When in doubt avoid RPC. If you can, you should use an asynchronous pipeline - instead of RPC-like blocking, results are asynchronously pushed to a next computation stage.

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
- https://www.rabbitmq.com/tutorials/tutorial-six-python
