# k8s-project

A Kubernetes-based platform project demonstrating modern DevOps practices including containerization, CI/CD, Kubernetes deployment, observability, and automated scaling.

## Overview

This project began as a Kubernetes learning exercise and evolved into a reusable platform foundation for future projects.

Current capabilities include:

- Flask application deployment
- Docker containerization
- GitHub Actions CI pipeline
- GitHub Container Registry (GHCR)
- K3s Kubernetes cluster
- Traefik ingress
- ConfigMaps and Secrets
- Horizontal Pod Autoscaling (HPA)
- Prometheus metrics collection
- Grafana dashboards and visualization

## Architecture

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
GitHub Container Registry (GHCR)
   │
   ▼
K3s Cluster
   │
   ├── Traefik Ingress
   ├── Deployment
   ├── Service
   ├── ConfigMap
   ├── Secret
   ├── HPA
   └── ServiceMonitor
           │
           ▼
      Prometheus
           │
           ▼
        Grafana
```

## Project Structure

```text
k8s-project/
├── .github/
│   └── workflows/
│       └── docker-build.yml
├── app/
│   ├── main.py
│   └── requirements.txt
├── k8s/
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   ├── secrets.yaml
│   ├── servicemonitor.yaml
│   ├── grafana-ingress.yaml
│   └── prometheus-ingress.yaml
├── Dockerfile
├── Makefile
├── .gitignore
└── README.md
```

## Features

### CI/CD

GitHub Actions automatically:

- Builds container images
- Pushes images to GitHub Container Registry
- Maintains `latest` and commit-specific image tags

Example image:

```text
ghcr.io/<github-username>/k8s-project:latest
```

### Kubernetes Deployment

The application is deployed to a K3s cluster using:

- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- Horizontal Pod Autoscaler

### Observability

Application metrics are exposed via:

```text
/metrics
```

Metrics are collected by Prometheus and visualized in Grafana.

Example custom metric:

```text
app_requests_total
```

### Autoscaling

The application automatically scales based on CPU utilization.

Current configuration:

```text
Min Pods: 2
Max Pods: 5
Target CPU: 50%
```

## Example Local DNS Configuration

Example hosts entries for a homelab environment:

```text
<k3s-node-ip> k8s-project.local
<k3s-node-ip> grafana.k8s-project.local
<k3s-node-ip> prometheus.k8s-project.local
```

Replace `<k3s-node-ip>` with the IP address of your Kubernetes node.

## Monitoring Stack

Installed using Helm:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install kube-prometheus-stack \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
```

Components include:

- Prometheus
- Grafana
- Alertmanager
- kube-state-metrics
- node-exporter

## Learning Objectives

This project demonstrates:

- Docker
- Kubernetes
- K3s
- GitHub Actions
- GitHub Container Registry
- Prometheus
- Grafana
- Traefik
- Horizontal Pod Autoscaling
- Service Discovery
- Ingress Management
- Containerized Application Delivery
- Observability and Monitoring

## Future Roadmap

### Platform Operations Dashboard

Potential future project focused on:

- Service catalog
- Deployment tracking
- Cluster health
- Platform observability
- Internal developer portal concepts

### Support Operations Dashboard

Potential future project focused on:

- Customer health metrics
- Support KPIs
- SLA tracking
- CSAT reporting
- Operational visibility for support leadership

## Security Notes

This repository intentionally excludes:

- API keys
- Access tokens
- Private certificates
- SSH keys
- kubeconfig files
- Production credentials

All example secrets and configuration values are placeholders only.

## Status

Current Status: Operational

Verified Components:

- GitHub Actions
- GitHub Container Registry
- K3s
- Traefik
- ConfigMaps
- Secrets
- Horizontal Pod Autoscaling
- Prometheus
- Grafana
- ServiceMonitor
- Application Metrics

This repository serves as the foundational platform for future DevOps and Operations-focused projects.
