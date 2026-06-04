# Kubernetes Interview Demo

## Overview

This project demonstrates the deployment and operation of a containerized Python Flask application on Kubernetes. The goal of the project is to gain hands-on experience with core cloud-native technologies including Docker, Kubernetes, ingress routing, autoscaling, configuration management, secrets management, and monitoring.

The application is deployed to a local Kubernetes cluster and includes several production-oriented concepts such as health checks, resource limits, autoscaling, ingress routing, and observability tooling.

---

## Technologies Used

### Application

* Python
* Flask

### Containerization

* Docker

### Kubernetes

* Deployment
* Service
* ConfigMap
* Secret
* Horizontal Pod Autoscaler (HPA)
* Ingress

### Observability

* Prometheus
* Grafana
* Metrics Server

### Tooling

* kubectl
* Helm
* Git
* GitHub

---

## Architecture

```text
User
  ↓
Ingress
  ↓
Service
  ↓
Deployment
  ↓
Pods
  ↓
Flask Application
```

Supporting Components

```text
ConfigMap
Secret
HPA
Prometheus
Grafana
```

---

## Features Implemented

### Containerized Flask Application

A simple Flask application was created and packaged into a Docker image.

Endpoints:

* `/`
* `/health`

The root endpoint returns:

* Environment information
* Pod hostname
* ConfigMap values
* Secret injection validation

---

### Kubernetes Deployment

The application is deployed using a Kubernetes Deployment.

Features:

* Multiple replicas
* Rolling updates
* Self-healing pods
* Declarative desired state

---

### Service

A ClusterIP Service provides stable networking and load balancing between application pods.

---

### ConfigMap

Application configuration is externalized through a ConfigMap.

Examples:

* APP_ENV
* APP_MESSAGE

This allows the same container image to be reused across environments without rebuilding.

---

### Secret Management

Sensitive configuration is injected using Kubernetes Secrets.

Example:

* API_KEY

The application validates that the secret is present without exposing the value.

---

### Health Checks

The deployment includes:

#### Readiness Probe

Determines when a pod is ready to receive traffic.

#### Liveness Probe

Determines when Kubernetes should restart a pod.

---

### Resource Management

Resource requests and limits were implemented to improve scheduling and prevent resource contention.

Example:

* CPU Requests
* CPU Limits
* Memory Requests
* Memory Limits

---

### Horizontal Pod Autoscaler

An HPA was configured to automatically scale the deployment based on CPU utilization.

Configuration:

* Minimum Replicas: 2
* Maximum Replicas: 5
* Target CPU Utilization: 50%

Testing confirmed successful scale-out from 2 replicas to 5 replicas under load.

---

### Ingress

NGINX Ingress was configured to expose the application through a hostname.

Example:

```text
http://k8s-demo.local
```

Traffic flow:

```text
Ingress Controller
    ↓
Ingress Rule
    ↓
Service
    ↓
Pods
```

---

### Monitoring and Observability

The kube-prometheus-stack Helm chart was deployed.

Components:

* Prometheus
* Grafana
* Alertmanager
* Node Exporter
* kube-state-metrics

These components provide:

* Cluster monitoring
* Node monitoring
* Pod monitoring
* Dashboard visualization

---

## Troubleshooting Experience

During development several common Kubernetes issues were encountered and resolved:

### CrashLoopBackOff

Cause:

* Missing Python dependency

Resolution:

* Rebuilt Docker image with correct requirements

---

### CreateContainerConfigError

Cause:

* Incorrect ConfigMap and Secret configuration

Resolution:

* Corrected Kubernetes manifests and environment references

---

### Kubernetes API Version Errors

Cause:

* Incorrect resource API versions

Examples:

* apps/v3
* apps/v2

Resolution:

* Corrected resources to appropriate API groups

---

### Application Startup Failure

Cause:

* Python syntax error

Resolution:

* Reviewed pod logs
* Corrected code
* Rebuilt image
* Rolled deployment

---

## Key Concepts Practiced

* Docker image creation
* Kubernetes deployments
* Service networking
* ConfigMap management
* Secret management
* Health probes
* Resource management
* Horizontal scaling
* Ingress routing
* Monitoring and observability
* Git workflows
* Kubernetes troubleshooting

---

## Future Improvements

Planned enhancements include:

* Application Prometheus metrics
* ServiceMonitor integration
* Grafana dashboards
* GitHub Actions CI/CD pipeline
* Helm chart packaging
* Deployment to dedicated Linux homelab infrastructure

---

## Learning Outcome

This project was built to develop practical Kubernetes and DevOps skills through hands-on implementation rather than isolated tutorials. The project demonstrates an end-to-end workflow including application deployment, configuration management, autoscaling, ingress routing, monitoring, and operational troubleshooting.
