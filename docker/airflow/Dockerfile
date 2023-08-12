# Base Image
FROM python:3.7-slim-bullseye
LABEL maintainer="MarcLamberti"

# Arguments that can be set with docker build
ARG AIRFLOW_VERSION=2.4.2
ARG AIRFLOW_HOME=/usr/local/airflow
# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Export the environment variable AIRFLOW_HOME where airflow will be installed
ENV AIRFLOW_HOME=${AIRFLOW_HOME}

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

COPY ./requirements-python3.7.txt /requirements-python3.7.txt

# Install dependencies and tools


RUN apt-get update -y && \
    apt-get upgrade -yqq && \
    apt-get install -yqq --no-install-recommends \
    python3-dev \
    wget \
    libczmq-dev \
    curl \
    libssl-dev \
    git \
    inetutils-telnet \
    bind9utils freetds-dev \
    libkrb5-dev \
    libsasl2-dev \
    libffi-dev libpq-dev \
    freetds-bin build-essential \
    default-libmysqlclient-dev \
    apt-utils \
    rsync \
    zip \
    unzip \
    gcc \
    vim \
    netcat \
    && apt-get autoremove -yqq --purge && apt-get clean

# Upgrade pip
# Create airflow user 
# Install apache airflow with subpackages
RUN pip install psycopg2 

RUN pip install --upgrade "pip==20.2.4" && \
    useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow && \
    pip install apache-airflow==${AIRFLOW_VERSION} --constraint /requirements-python3.7.txt && \
    pip install apache-airflow-providers-apache-hdfs==2.1.0 && \
    pip install apache-airflow-providers-apache-hive==2.0.2 && \
    pip install apache-airflow-providers-apache-spark==2.0.1 && \
    pip install apache-airflow-providers-slack==4.0.1 && \
    pip install apache-airflow-providers-http==2.0.1 && \
    pip install 'redis==3.2'
# Copy the airflow.cfg file (config)
#COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# Set the owner of the files in AIRFLOW_HOME to the user airflow
COPY script/entrypoint.sh /entrypoint.sh
#COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

RUN chown -R airflow: ${AIRFLOW_HOME}

#COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
# Set the username to use
USER airflow

# Create the folder dags inside $AIRFLOW_HOME
RUN mkdir -p ${AIRFLOW_HOME}/dags

# Expose ports (just to indicate that this container needs to map port)
EXPOSE 8080 5555 8793

# Execute start-airflow.sh
USER airflow
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"] # set default arg for entrypoint    