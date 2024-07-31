# rabbitmq-tutorial
Following RabbitMQ tutorials in order to learn basic concepts.

## Useful commands

```sh
# run RabbitMQ server
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:latest
```

```sh
# create virtual environment
python3 -m venv venv
# activate virtual environment
source venv/bin/activate
```

```sh
# update requirements.txt
pip freeze > requirements.txt
```
