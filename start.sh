#!/bin/bash
docker build -t hadoop-base docker/hadoop/hadoop-base && \
docker build -t hive-base docker/hive/hive-base && \
docker build -t spark-base docker/spark/spark-base && \
docker-compose -f docker-compose-CeleryExecutor.yml up -d
