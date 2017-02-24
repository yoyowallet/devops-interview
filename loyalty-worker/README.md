# Loyalty Worker

This service is a worker that processes transactions from a message queue and awards loyalty stamps and vouchers as appropriate.

For now, this service is a work-in-progress and only prints transaction to the console.

## Dependencies

- Python 3.6+
- Redis

## Quickstart

Example:

```bash
$ python --version
Python 3.6.0
$ redis-cli ping
PONG
$ pip install -r requirements.txt
$ export HTTP_PORT=5000
$ export REDIS_URL=redis://127.0.0.1:6379/0
$ python run.py
12:00:00 RQ worker 'rq:worker:jian.1337' started, version 0.7.1
12:00:00 Cleaning registries for queue: default
12:00:00
12:00:00 *** Listening on default...
```

## Environment variables

| Environment variable | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| HTTP_PORT            | **Required**. Port to bind HTTP server. Default: `5000`.     |
| REDIS_URL            | **Required**. Redis URL. Default: `redis://127.0.0.1:6379/0` |
