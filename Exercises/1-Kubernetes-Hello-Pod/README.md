Exercise 1: Kubernetes Hello Pod

Business Problem — Zepto Example

Imagine working as a DevOps Engineer at Zepto. The product team has created a lightweight web application representing the storefront and delivery-status page.

The task is to deploy the application on Kubernetes so that it can run reliably, remain portable, and be scaled later.

For this exercise, the Nginx container image is used to simulate Zepto’s web application.

Objective

Learn the basics of Kubernetes by:

* Starting a local Kubernetes cluster using Minikube
* Creating a Kubernetes Pod
* Running an Nginx container inside the Pod
* Exposing the Pod using a NodePort Service
* Accessing the application through Minikube

Prerequisites

The following tools were already installed:

* Docker
* Minikube
* kubectl

Step 1: Start Minikube

Start the local Kubernetes cluster:

minikube start --driver=docker

Verify the cluster:

minikube status

The Minikube control plane, kubelet, and API server were successfully started.

Step 2: Create the Nginx Pod

Create a Pod using the official Nginx image:

kubectl run hello-k8s --image=nginx --port=80

Output:

pod/hello-k8s created

Step 3: Verify the Pod

Check the Pods:

kubectl get pods

The hello-k8s Pod reached the Running state with the container ready.

Step 4: Expose the Pod

Expose the Nginx Pod using a NodePort Service:

kubectl expose pod hello-k8s --type=NodePort --port=80

Verify the Service:

kubectl get services

The resulting Service was:

hello-k8s    NodePort    ...    80:30815/TCP

The NodePort may vary each time Kubernetes creates the Service.

Step 5: Access the Application

Access the Service using:

minikube service hello-k8s

Minikube opened the Nginx application in the browser.

The standard Nginx welcome page was displayed, confirming that the application was successfully deployed and exposed through Kubernetes.

Kubernetes Concepts Learned

Pod

A Pod is the smallest deployable unit in Kubernetes. It can contain one or more containers that share networking and storage resources.

In this exercise, the Pod named hello-k8s contains the Nginx container.

Service

A Kubernetes Service provides a stable way to access Pods.

The hello-k8s Service was created with the NodePort type.

NodePort

NodePort exposes a Service on a port available on the Kubernetes node, allowing applications inside the cluster to be accessed externally.

Minikube

Minikube provides a local Kubernetes cluster suitable for learning, development, and testing.

kubectl

kubectl is the command-line interface used to interact with and manage Kubernetes resources.

Useful Commands

Start Minikube:

minikube start

Check cluster status:

minikube status

Create a Pod:

kubectl run hello-k8s --image=nginx --port=80

List Pods:

kubectl get pods

Expose a Pod:

kubectl expose pod hello-k8s --type=NodePort --port=80

List Services:

kubectl get services

Open a Minikube Service:

minikube service hello-k8s

Result

The Nginx container was successfully deployed as a Kubernetes Pod and exposed using a NodePort Service. The Nginx welcome page was successfully accessed through Minikube.
