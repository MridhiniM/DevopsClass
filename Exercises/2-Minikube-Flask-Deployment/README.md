Exercise 2: Deploy a Flask App on Minikube Using kubectl and YAML

Objective

Deploy a simple Python Flask application on a local Kubernetes cluster using Minikube, Docker, kubectl, and Kubernetes YAML configuration.

Project Structure

2-Minikube-Flask-Deployment/
├── app.py
├── Dockerfile
├── flask-deployment.yaml
└── README.md

1. Start Minikube

minikube start --driver=docker

Verify the cluster:

minikube status
kubectl get nodes

The Minikube node was successfully shown as Ready.

2. Flask Application

The Flask application runs on port 15000.

from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello from Flask on Kubernetes!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)

3. Build the Docker Image

The Flask application was packaged using the following Dockerfile:

FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python", "app.py"]

The image was built using:

docker build -t flask-app .

The image was then loaded into Minikube:

minikube image load flask-app

4. Kubernetes Deployment

The application was deployed using flask-deployment.yaml.

The Deployment creates one replica and exposes container port 15000.

kubectl apply -f flask-deployment.yaml

Verify the Deployment:

kubectl get deployments

Verify the Pod:

kubectl get pods -l app=flask-app

The pod reached the Running state with 1/1 containers ready.

5. Inspect the Deployment

kubectl describe deployment flask-app

The Deployment showed:

* 1 desired replica
* 1 available replica
* Image: flask-app:latest
* Container port: 15000
* Deployment status: Available

6. Check Application Logs

kubectl logs <pod-name>

The logs confirmed that Flask was running on:

0.0.0.0:15000

7. Create a Kubernetes Service

A NodePort Service was added to the YAML configuration:

apiVersion: v1
kind: Service
metadata:
  name: flask-app-service
spec:
  selector:
    app: flask-app
  ports:
  - port: 15000
    targetPort: 15000
  type: NodePort

The configuration was applied using:

kubectl apply -f flask-deployment.yaml

8. Access the Flask Application

The Service URL was obtained using:

minikube service flask-app-service --url

The generated URL was:

http://127.0.0.1:61619

Testing the endpoint with:

curl http://127.0.0.1:61619

returned:

Hello from Flask on Kubernetes!

Questions and Answers

1. What is the purpose of minikube service flask-app-service --url?

It provides a URL that can be used to access the Kubernetes Service from the local machine.

2. What happens when this command is executed?

Minikube identifies the specified Service and creates/provides a local URL through which the Service can be accessed.

3. Why is targetPort required?

targetPort specifies the port on which the application is listening inside the container.

4. What is the difference between port and targetPort?

* port is the port exposed by the Kubernetes Service.
* targetPort is the port on the application container to which traffic is forwarded.

5. How can a Flask application running in Minikube be accessed?

A Service can be exposed and accessed using:

minikube service <service-name> --url

6. Why does the terminal need to remain open when using the Docker driver on macOS?

Minikube maintains the local connection/tunnel required to expose the Service URL when using the Docker driver.

7. What is the benefit of using --url?

It provides a convenient local URL for accessing the Kubernetes Service without manually determining the NodePort.

8. How can an application be exposed in Kubernetes?

An application can be exposed using:

kubectl expose

or by defining a Kubernetes Service in a YAML file and applying it with:

kubectl apply -f <service.yaml>

9. How does Minikube help with Kubernetes development?

Minikube provides a local Kubernetes cluster, allowing applications and Kubernetes configurations to be developed and tested without requiring a remote cluster.

10. What is kubectl?

kubectl is the Kubernetes command-line tool used to interact with and manage Kubernetes clusters, including deploying applications, inspecting resources, viewing logs, and managing Services.
