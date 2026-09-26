Exercise 4 — Docker Networking

Objective

The objective of this exercise is to understand Docker networking by creating a user-defined bridge network and running multiple containers that communicate with each other using Docker’s internal DNS.

1. Create a Docker Bridge Network

Created a user-defined bridge network using:

docker network create --driver bridge my-bridge-net

The network was verified using:

docker network ls
docker network inspect my-bridge-net

2. Flask REST API

Created a simple Flask REST API with an /about endpoint.

app.py

from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        "name": "Simple REST API",
        "version": "1.0",
        "description": "This is a simple REST API built with Flask."
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

The Docker image was built using:

docker build --no-cache -t flask-api .

The Flask container was started with:

docker run -d \
  --name flask \
  --network my-bridge-net \
  -p 5001:5001 \
  flask-api

The API was tested using:

curl http://localhost:5001/about

Result:

{
    "description": "This is a simple REST API built with Flask.",
    "name": "Simple REST API",
    "version": "1.0"
}

3. MySQL Container

MySQL was started using:

docker run -d \
  --name mysql \
  --network my-bridge-net \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=testdb \
  mysql:8.0

4. Redis Container

Redis was started using:

docker run -d \
  --name redis \
  --network my-bridge-net \
  redis:7

5. Container Networking

All three containers were connected to the same user-defined bridge network:

my-bridge-net
│
├── flask
├── mysql
└── redis

The network was inspected using:

docker network inspect my-bridge-net

Docker assigned private IP addresses to each container.

The containers were also able to resolve each other by their container names using Docker’s internal DNS.

For example:

docker exec flask python -c "import socket; print(socket.gethostbyname('mysql'))"

and:

docker exec flask python -c "import socket; print(socket.gethostbyname('redis'))"

successfully resolved the MySQL and Redis container names.

6. Connectivity Tests

The Flask container was used to test connectivity to the other containers.

Flask → MySQL

docker exec -it flask bash
ping -c 4 mysql

The ping was successful with 0% packet loss.

Flask → Redis

ping -c 4 redis

The ping was successful with 0% packet loss.

This demonstrates that containers attached to the same user-defined bridge network can communicate with one another using container names.

⸻

Questions

1. What is the difference between the default bridge network and a user-defined bridge network?

The default Docker bridge network provides basic container networking, but containers on it generally require IP addresses for direct communication.

A user-defined bridge network provides additional features such as automatic DNS-based service discovery. Containers on the same user-defined network can communicate using their container names instead of manually finding their IP addresses.

For example:

flask → mysql
flask → redis

Docker resolves mysql and redis to the appropriate container IP addresses.

⸻

2. Why is it important for containers to communicate with each other in a microservices architecture?

Microservices applications are commonly divided into separate services, with each service running independently.

These services need to communicate with one another. Docker networking provides isolated networks that allow services to communicate securely and reliably.

For example:

Frontend → API → Database
             │
             └──→ Cache

Docker networks allow these services to communicate without exposing every service directly to the host machine.

⸻

3. How does Docker’s DNS service help in container communication?

Docker provides an internal DNS service for user-defined networks.

Instead of using changing container IP addresses, containers can use container names as hostnames.

For example:

mysql
redis

Docker automatically resolves these names to the corresponding container IP addresses.

This is useful because container IP addresses can change when containers are recreated, while the container/service name can remain the same.

⸻

4. What happens if you try to ping a container not connected to the same network?

Containers that are not connected to the same Docker network generally cannot communicate with each other through that network.

For example, if flask is connected to my-bridge-net but another container is connected only to a different network, flask will not be able to resolve or directly communicate with that container through my-bridge-net.

This network isolation helps Docker applications separate different groups of services.

⸻

Conclusion

The exercise demonstrated how Docker’s user-defined bridge networks allow multiple containers to communicate using container names through Docker’s internal DNS.

The final setup consisted of:

                 my-bridge-net
                       │
          ┌────────────┼────────────┐
          │            │            │
       flask         mysql        redis
       :5001         :3306        :6379
          │
          │
     localhost:5001
          │
          ▼
         Host

The Flask API was successfully accessed from the host machine, and connectivity from Flask to both MySQL and Redis was successfully verified.