# Python-RabbitMQ Event-Driven Architecture Demo

## Short Description

This is a simple project demonstrating the **Event-Driven Architecture (EDA)** utilizing RabbitMQ as the message broker & Python to publish/subscribe messages. The project is configured using the **UV** package manager. For the demonstration purpose, RabbitMQ is configured in the Docker container.

## Objectives

1. Setup RabbitMQ in Docker of local machine.
2. Configure **UV** to run the Python scripts.
3. Build a producer to publish & consumer to consume messages through the RabbitMQ message broker.

## How to Setup

1.  Install UV package manager if it doesn't exist in the local machine.

        pip install uv

2.  Install the required packages from "requirements.txt" file.

        uv add -r requirements.txt

3.  Run the script named "consumer.py" in a different terminal.

        uv run producer.py

4.  Run the script named "producer.py" in a different terminal.

        uv run consumer.py

## RabbitMQ Setup: Docker Container

Execute the following command to locally download the image (_if doesn't exist_) & run a RabbitMQ container.

    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management

It will run the container with a <u>RabbitMQ management dashboard</u> and anyone can access the dashboard by typing "http://localhost:15672" in the browser. By default, for accessing into the dashboard from the browser, use the `guest` & `guest` accordingly for the username & password.

The other port (_5672_) is used by the Python code to **publish/subcribe messages** to the message broker.

**Note:** To persist the volume of the container, include the `-v` or `--volume` command, so that Docker will mount a volume from the local machine while spinning up the container.

    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 --volume <your-local-machine-path>:/var/lib/rabbitmq rabbitmq:4-management
