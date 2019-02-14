SET UP

Prerequisites
: Intall Docker following the installation guide choosing the right platform (Mac) https://docs.docker.com/docker-for-mac/install/

Obtaining the Docker Image - Download the Docker image from Docker Hub
: Choose the Docker image (Jupyter/PySpark-Notebook) from Docker Hub https://hub.docker.com/r/jupyter/pyspark-notebook/. The image is automatically built based on the Dockerfile.

Running the Docker image with Two Containers - Web App and ML Model & API

1) Define settings in Dockerfile for each container (e.g., EXPOSE, RUN, ADD, CMD)
2) Define the services in docker-compose.yml so they can be run together in an isolated environment. In this case, services are a web app and ML model & API. In a compose file, define how these services link together, any volumes needed to be mounted inside the containers and defines which portstheses services expose. 

For this assignment, I used ADD in Dockerfile for each service to copy relevant files to a container and linked defined two services web app and ml api so that the recieved input data through web app can be sent to the api container (web is linked to api). Also, the web app listens the port 8080 and the api listens the port 8081 and linked host's port to the docker container with the same port number.



RUN THE APPLICATION

Build the Images

"docker-compose build"
: The docker-compose build reads docker-compose.yml and build all the services defined in there.

Start Services

"docker-compose up"
: Instructs to Compose to run the services defined in the docker-compose.yml in containers.

Stop Containers

"docker-compose down"
: Stops and Removes the service containers

"docker-compose stop"
: Stops the service containers without removing them

"docker rmi (image-id or name)"
: Removes the images

Submitting Input Data 
: Go on to http://0.0.0.0:8080/ on the web.
: Input feature values and the result would be printed out on the console as "Result: ".




