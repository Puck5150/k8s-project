# Kubernetes Interview Demo

## Overview

This project demonstrates the deployment, operation, scaling, and monitoring of a containerized Python Flask application running on Kubernetes.

The goal of the project is to build practical experience with modern DevOps and cloud-native tooling while implementing concepts commonly used in production environments.

The application is deployed to a local Kubernetes cluster and includes:

* Containerization with Docker
* Kubernetes Deployments and Services
* ConfigMap and Secret management
* Health probes
* Horizontal Pod Autoscaling (HPA)
* Ingress routing
* Prometheus monitoring
* Grafana dashboards
* Application metrics instrumentation
* ServiceMonitor-based metrics discovery

---

# Architecture

```text
                        ┌─────────────────┐
                        │     Grafana     │
                        └────────┬────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │   Prometheus    │
                        └────────┬────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │ ServiceMonitor  │
                        └────────┬────────┘
                                 │
                                 ▼

User
 │
 ▼
Ingress
 │
 ▼
Service
 │
 ▼
Deployment
 │
 ▼
Pods
 │
 ▼
Flask Application
```

Supporting Kubernetes Resources:

* ConfigMap
* Secret
* Horizontal Pod Autoscaler
* ServiceMonitor

---

# Technologies Used

## Application

* Python
* Flask

## Containerization

* Docker

## Kubernetes

* Deployment
* Service
* ConfigMap
* Secret
* Ingress
* Horizontal Pod Autoscaler
* ServiceMonitor

## Monitoring

* Prometheus
* Grafana
* kube-prometheus-stack
* Metrics Server

## Tooling

* Helm
* Git
* GitHub
* kubectl

---

# Features

## Flask Application

A lightweight Flask application provides:

### Endpoints

| Endpoint | Purpose                 |
| -------- | ----------------------- |
| /        | Application information |
| /health  | Health check            |
| /metrics | Prometheus metrics      |

The application returns:

* Environment information
* Pod hostname
* ConfigMap values
* Secret validation status

Example:

```json
{
  "message": "Hello from ConfigMap",
  "environment": "local-kubernetes",
  "hostname": "k8s-interview-demo-xxxxx",
  "api_key_loaded": true
}
```

---

## Docker

The application is containerized using Docker.

The image includes:

* Python runtime
* Flask application
* Prometheus client library

---

## Kubernetes Deployment

The application is deployed using a Kubernetes Deployment.

Features:

* Multiple replicas
* Rolling updates
* Self-healing pods
* Declarative desired state

---

## Kubernetes Service

A ClusterIP Service provides:

* Stable networking
* Internal load balancing
* Service discovery

---

## ConfigMap

Application configuration is externalized using a ConfigMap.

Examples:

* APP_ENV
* APP_MESSAGE

Benefits:

* Configuration separated from code
* Reusable container images
* Environment-specific configuration

---

## Secret Management

Sensitive values are stored in Kubernetes Secrets.

Example:

* API_KEY

The application verifies the secret exists without exposing the value.

---

## Health Probes

### Readiness Probe

Determines when a pod is ready to receive traffic.

### Liveness Probe

Determines when Kubernetes should restart a pod.

Benefits:

* Improved availability
* Automatic recovery

---

## Resource Requests and Limits

CPU and memory requests/limits are configured.

Benefits:

* Predictable scheduling
* Resource isolation
* Reduced noisy-neighbor issues

---

## Horizontal Pod Autoscaler

The deployment automatically scales based on CPU utilization.

Configuration:

* Minimum Replicas: 2
* Maximum Replicas: 5
* Target CPU Utilization: 50%

Testing confirmed automatic scaling from:

```text
2 Pods
  ↓
5 Pods
```

under generated load.

---

## Ingress

NGINX Ingress routes traffic into the cluster.

Example:

```text
http://k8s-demo.local
```

Traffic Flow:

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

# Monitoring and Observability

## Prometheus

Prometheus is deployed using the kube-prometheus-stack Helm chart.

Collected Metrics:

* Node metrics
* Kubernetes metrics
* Deployment metrics
* Pod metrics
* Application metrics

---

## Grafana

Grafana provides visualization and dashboards for:

* Cluster health
* Node utilization
* Pod utilization
* Deployment status
* Application metrics

---

## Application Metrics

The Flask application exposes Prometheus metrics via:

```text
/metrics
```

Custom metrics include:

### Request Counter

```text
app_requests_total
```

Tracks the total number of requests received by the application.

Example:

```promql
app_requests_total
```

---

## ServiceMonitor

A ServiceMonitor automatically registers the application with Prometheus.

Discovery Flow:

```text
Prometheus
     ↓
ServiceMonitor
     ↓
Service
     ↓
Pods
     ↓
/metrics
```

This enables automatic scraping without manual Prometheus configuration.

---

# Troubleshooting Experience

Several common Kubernetes issues were encountered and resolved.

## CrashLoopBackOff

Cause:

* Missing Python dependency

Resolution:

* Updated requirements.txt
* Rebuilt container image
* Redeployed application

---

## CreateContainerConfigError

Cause:

* Invalid ConfigMap/Secret references

Resolution:

* Corrected Kubernetes manifests
* Redeployed workload

---

## Kubernetes API Version Errors

Cause:

* Invalid API versions

Examples:

* apps/v2
* apps/v3

Resolution:

* Corrected resource definitions

---

## Application Startup Failure

Cause:

* Python syntax error

Resolution:

* Reviewed pod logs
* Corrected code
* Rebuilt image
* Performed rolling deployment

---

## Prometheus Discovery Issues

Cause:

* Missing ServiceMonitor configuration

Resolution:

* Added ServiceMonitor
* Verified target registration
* Confirmed metrics ingestion

---

# Skills Demonstrated

* Linux Administration
* Docker
* Kubernetes
* Ingress
* Autoscaling
* Monitoring
* Observability
* Prometheus
* Grafana
* Configuration Management
* Secrets Management
* Git Workflows
* Troubleshooting
* Operational Diagnostics

---

# Future Improvements

Planned enhancements:

* GitHub Actions CI/CD pipeline
* Helm packaging
* Alertmanager integrations
* Custom Grafana dashboards
* Persistent storage
* Deployment to dedicated Linux homelab
* Multi-node Kubernetes cluster
* GitOps workflow implementation

---

# Learning Outcome

This project was created to develop practical experience with Kubernetes and cloud-native operations through hands-on implementation rather than isolated tutorials.

The project demonstrates the complete lifecycle of a modern application including deployment, configuration management, autoscaling, ingress routing, monitoring, observability, and troubleshooting.
