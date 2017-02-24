#!/usr/bin/env python
import os

from redis import StrictRedis
from rq import Connection
from rq import Worker


def record_transaction(*, user_id: int, amount: int, currency: str):
    # TODO: persist to database
    print(f'==> Recording transaction: User ID: {user_id}, Amount: {amount}, Currency: {currency}')


if __name__ == '__main__':
    redis_url: str = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/0')

    conn = StrictRedis.from_url(redis_url)

    with Connection(conn):
        worker = Worker('default')
        worker.work()
