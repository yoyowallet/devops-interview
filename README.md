# Yoyo Wallet DevOps Interview Test

## Background

Yoyo Wallet is a building a microservices-based platform.

As a DevOps engineer, you are tasked with improving the engineering efficiency by producing automation tools
that provision services in an efficient, predictable and reproducible way.

We use [HTTPie](https://github.com/jkbrzt/httpie) in our examples for clarity.

## Architecture Overview

```
                      +-------------------------------------------+
                      |                                           |
                      |             Redis Message Queue           |
                      |                                           |
                      +--------^--------------------------+-------+
                               |                          |
                              (4)                        (6)
                               |                          |
+------------+       +---------+---------+      +---------v--------+
|            |       |                   |      |                  |
|  Auth API  |       |  Transaction API  |      |  Loyalty Worker  | (*n)
|            |       |                   |      |                  |
+--^------+--+       +---^-----------+---+      +------------------+
   |      |              |           |
  (1)    (2)            (3)         (5)
   |      |              |           |
+--+------v--------------+-----------v----+
|                                         |
|                Customer                 |
|                                         |
+-----------------------------------------+
```

There are 3 distinct services:

- [Auth API] - Creates authentication tokens to valid users.
- [Transaction API] - Processes transaction requests.
- [Loyalty Worker] - Processes loyalty from transactions.

A transaction flow is as follows:

1. A customer authenticates with the [Auth API] by providing a valid username and password.
2. An authentication token that is valid for 30 seconds is returned.
3. Use this authentication token to make a transaction request to the [Transaction API].
4. The [Transaction API] submits the transaction to a message queue for further background processing.
5. A successful response is returned.
6. Meanwhile, a [Loyalty Worker] processes the transaction from the message queue by awarding stamps and vouchers as appropriate.

We use environment variables to configure a service.

## Your task

- Read the documentation for each service. Run and test them to make sure they work as expected.
- Once you're familiar with the services, use your preferred tools to automate provisioning of a **local development** environment.
- Be sure to include external dependencies like Redis and configuration management.
- In order for a microservices-based architecture to work best, implement a HTTP router in front of the services that routes
  requests to the correct service. A popular solution is path-based routing:
    - http://platform/authentication/* → http://authentication-api/*
    - http://platform/transactions/* → http://transactions-api/*
- Make your automation available on a public GitHub repository with a `README` on how to get things started.

Don't worry too much about making this production ready. We may discuss production considerations with you later on.

## Bonus (Optional)

- Containerise services.
- Apply the [Twelve Factor App](https://12factor.net/) methodology.

[Auth API]: auth-api
[Transaction API]: transaction-api
[Loyalty Worker]: loyalty-worker
