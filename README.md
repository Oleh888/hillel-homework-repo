# hillel-homework-repo

## HW-10 Docker

This repository contains a Dockerfile for building a Java application using Maven and running it with a lightweight JRE.

### Building docker image locally

Navigate to the `hw10` folder and use the following command to build the Docker image.

```bash
docker build -t docker-demo-app:v1.0 .
```

Use the command below to run the Docker demo application in a container.

```bash
docker run -p 8080:8080 --name demo-app docker-demo-app:v1.0
# The -p option maps port 8080 from the container to port 8080 on the host.
```

To check if the application is running, execute a curl command.

```bash
curl localhost:8080
# Replace 'localhost' with the actual hostname or IP address of your Docker host.
```

## HW-16 Jenkins