# Kubernetes Interview Demo

Simple Flask API containerized with Docker and deployed to Kubernetes.

## Features

- Dockerized Python Flask app
- Kubernetes Deployment
- Kubernetes Service
- Readiness and liveness probes
- Horizontal scaling demo

## Build

docker build -t k8s-interview-demo:v1 .

## Deploy

kubectl apply -f k8s/

## Test

kubectl port-forward svc/k8s-interview-demo 8080:80

curl http://localhost:8080