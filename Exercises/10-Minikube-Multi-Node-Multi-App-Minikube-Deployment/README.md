# Exercise 10: Minikube Multi-Node Multi-App Deployment

## Objective
Deploy two Flask applications on a three-node Minikube cluster using Docker images, Kubernetes Deployments, and NodePort Services.

## Architecture
- Minikube profile: multi-app-cluster
- Nodes: 1 control-plane node and 2 worker nodes
- Product Catalog: 2 replicas
- Shopping Cart: 3 replicas
- Container port: 5000
- Product Catalog NodePort: 30081
- Shopping Cart NodePort: 30082

## Applications

### Product Catalog
- `/` - Service health message
- `/products` - Returns the product list as JSON

### Shopping Cart
- `/` - Service health message
- `/cart` - Returns shopping cart items
- `/cart/add` - Adds an item using a POST request with JSON data

## Project Structure
- `product-catalog/` - Flask application, requirements, and Dockerfile
- `shopping-cart/` - Flask application, requirements, and Dockerfile
- `k8s/` - Kubernetes Deployment and Service manifests

## Build Docker Images

    docker build -t product-catalog:1.0 ./product-catalog
    docker build -t shopping-cart:1.0 ./shopping-cart

## Load Images into Minikube

    minikube -p multi-app-cluster image load product-catalog:1.0
    minikube -p multi-app-cluster image load shopping-cart:1.0

## Deploy Applications

    kubectl --context=multi-app-cluster apply -f k8s/product-catalog-deployment.yaml
    kubectl --context=multi-app-cluster apply -f k8s/shopping-cart-deployment.yaml
    kubectl --context=multi-app-cluster apply -f k8s/product-catalog-service.yaml
    kubectl --context=multi-app-cluster apply -f k8s/shopping-cart-service.yaml

## Verify Deployment

    kubectl --context=multi-app-cluster get nodes
    kubectl --context=multi-app-cluster get pods -o wide
    kubectl --context=multi-app-cluster get deployments
    kubectl --context=multi-app-cluster get services

## Access Services on macOS

Run each command in a separate terminal and keep both terminals open:

    minikube -p multi-app-cluster service product-catalog-service --url
    minikube -p multi-app-cluster service shopping-cart-service --url

Keep each tunnel terminal open while testing the returned URLs.

## Result
Both applications were deployed successfully. Product Catalog reached 2/2 ready replicas, and Shopping Cart reached 3/3 ready replicas. All five pods were Running across the three cluster nodes, and both applications' endpoints were tested.
