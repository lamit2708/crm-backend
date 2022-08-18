# Guidline for Docker Setup

##Create sample dockerfile
[REF](https://docs.docker.com/get-started/part2/#sample-dockerfile)
```bash
# Use the official image as a parent image.
FROM node:current-slim

# Set the working directory.
WORKDIR /usr/src/app

# Copy the file from your host to your current location.
COPY package.json .

# Run the command inside your image filesystem.
RUN npm install

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8080

# Run the specified command within the container.
CMD [ "npm", "start" ]

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .
```
## Permission Denied Error
https://www.edureka.co/community/68431/docker-permission-connect-socket-connect-permission-denied


    sudo useradd user-name

    sudo passwd user-name 

    sudo groupadd docker

    Sudo usermod -aG docker user-name

    Sudo chmod 777 /var/run/docker.sock
    
## Build your image
```bash
docker build --tag bulletinboard:1.0 .
```
## Start your image as a container
```bash
docker run --publish 8000:8080 --detach --name bb bulletinboard:1.0
```
Now, run localhost:8000 for test

## Stop container
```bash
docker stop bb
```
## Delete container
```bash
docker rm --force bb
```

## Share image on docker hub
```Python
docker login
docker tag bulletinboard:1.0 <Your Docker ID>/bulletinboard:1.0
docker push <Your Docker ID>/bulletinboard:1.0
```

## Check images
```bash
docker images
```

## Delete a image
```bash
docker rmi {image_id/name}
```
## List the running containers
```bash
docker ps
```

## List all containers
```bash
docker ps -a
```

## Delete a container
```bash
docker rm -f {container_id/name}
```
## Start a container
```bash
docker start {container_name}
```

## Access a running container
```bash
docker exec -it {container_name} /bin/bash
```
