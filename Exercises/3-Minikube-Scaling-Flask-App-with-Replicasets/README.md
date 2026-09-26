# Exercise 3 – Minikube Scaling Flask App with ReplicaSets

## Objective

Deploy a Flask application on a single-node Minikube Kubernetes cluster using a ReplicaSet.

The application is initially deployed with 3 replicas, scaled to 5 replicas, and tested for self-healing by deleting one of the Pods.

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── flashsale-replicaset.yaml
└── README.md
