# Scalable Microservice

Welcome to the Scalable Microservice Design project. This microservice is an educational project to help developers on your first challenge designing a system to handle API requests for data storage and retrieval with high performance and scalability. The service is built using Python FastAPI and utilizes MongoDB for data persistence. The architecture is designed to ensure that read/write operations are within 500ms, even as data scales to millions or billions of records.
With this project you can scale every piece that has a higher demand separately. 
---

# Table of Contents

- [Project Overview](#project-overview)
- [Architecture Overview](#architecture-overview)
- [Design Decisions](#design-decisions)
- [Setup Instructions](#setup-instructions)
- [Build, Test, and Deploy Instructions](#build-test-and-deploy-instructions)
- [CI/CD Pipeline Explanation](#cicd-pipeline-explanation)
- [Testing Strategy](#testing-strategy)
- [Kubernetes Deployment Design](#kubernetes-deployment-design)
- [Estimated Development Time](#estimated-development-time)
- [Conclusion](#conclusion)

---

## Architecture Overview

# Architecture Overview

The microservice follows a layered architecture to promote separation of concerns and scalability.

1. **API Layer**: Handles HTTP requests using FastAPI.
2. **Service Layer**: Contains business logic and data validation.
3. **Data Access Layer**: Interacts with MongoDB for data persistence.

**Technologies Used**:

- **FastAPI**: For building the API endpoints.
- **MongoDB**: Chosen for its scalability and performance with large datasets.
- **Docker**: Containerization of the application.
- **Kubernetes**: Deployment and orchestration.
- **GitHub Actions**: CI/CD pipeline for automated testing and deployment.

**Architectural Diagram**:

*Since visual diagrams cannot be displayed here, below is a textual representation.*
TODO: link diagram
```
+-------------------+
|    API Layer      |  <-- FastAPI Endpoints (POST /data, GET /data)
+-------------------+
           |
           v
+-------------------+
|   Service Layer   |  <-- Business Logic and Validation
+-------------------+
           |
           v
+-------------------+
| Data Access Layer |  <-- MongoDB Interactions
+-------------------+
```
---

# Design Decisions

## Language Choice: Python (FastAPI)

- **Rationale**: FastAPI is modern, is easy to programming, has documentation, and supports asynchronous operations, which are essential for high-performance applications.

## Database Choice: MongoDB

- **Rationale**: MongoDB offers horizontal scalability and high performance for read/write operations, suitable for handling large volumes of data.

## Containerization: Docker

- **Rationale**: Docker ensures consistency across different environments and simplifies deployment.

## Orchestration: Kubernetes

- **Rationale**: Kubernetes provides automated deployment, scaling, and management of containerized applications.

## CI/CD Pipeline: GitHub Actions

- **Rationale**: Seamless integration with GitHub repositories and supports automated workflows for testing and deployment.

---

# Setup Instructions

## Prerequisites

- **Python 3.11+**
- **Docker**
- **Kubernetes Cluster**
- **Make Commands**
- **Git**

## Clone the Repository

```bash
git clone https://github.com/DouglasMagno/scalable-microservice.git
cd scalable-microservice
```
## Environment Variables

Create a `.env` file in the root directory with the following content:

```env
MONGODB_URI=mongodb://mongo
DATABASE_NAME=your_database_name
```
## Build

```bash
make build
```
---
# Build, Test, and Deploy Instructions

## Building the Application

### Locally

```bash
make build up
```

## Testing the Application

```bash
make test
```
or one file:
```bash
make test-file FILE=tests/test_services.py
```
or by FastAPI openapi
```text
http://localhost/docs
```
---
# CI/CD Pipeline Explanation

The CI/CD pipeline is orchestrated using **GitHub Actions** and consists of the following steps:

1. **Code Integration**: On every push or pull request to the `main` branch.
2. **Automated Testing**: Runs unit tests using `pytest`.
3. **Containerization**: Builds a Docker image of the application.
4. **Deployment**: Deploys the Docker image to a Kubernetes cluster.

**CI/CD Pipeline Diagram**:

```
[Git Push] --> [GitHub Actions Triggered]
                  |
                  v
           [Automated Tests]
                  |
                  v
           [Docker Build]
                  |
                  v
           [Push to Registry]
                  |
                  v
          [Kubernetes Deploy]
```
---
# Testing Strategy

## Tests

- **Scope**: Core application functionality, including API endpoints, business logic, and data access layer.
- **Tools**: `pytest`.

---

# Kubernetes Deployment Design

## Kubernetes Manifest Files

- **Deployment**: Defines the desired state for deploying the microservice.
- **Service**: Exposes the deployment internally within the cluster.
- **Ingress**: (Optional) Manages external access to the services in the cluster.
- **ConfigMap**: Stores configuration data.
- **Secret**: Stores sensitive information like database credentials.

**Deployment Diagram**:

```
[Deployment]
     |
     v
[Pod with Container]
     |
     v
[Service (ClusterIP)]
     |
     v
[Ingress Controller]
     |
     v
[External Traffic]
```
## Steps to Deploy

1. **Apply Configurations**

```bash
kubectl apply -f k8s/mongo
kubectl apply -f k8s/app
```

2. **Verify Deployment**

```bash
kubectl get pods
kubectl get services
```
---

# Access the Application
```bash
kubectl port-forward service/scalable-microservice-service 80:80
```
and test link for FastAPI openapi
```text
http://localhost/docs
```

---
# Estimated Development Time

- **API Development**: 2 days
- **Unit Testing**: 1 day
- **Containerization**: 1 day
- **CI/CD Pipeline Setup**: 1 day
- **Kubernetes Deployment Configurations**: 1 day
- **Documentation**: 1 day

**Total Estimated Time**: **7 days**

---
# Best practices
- **Conventional commits**
- **Make commands to automate development**
- **Structured module folders in your domain**
- **Tests scenarios and described flow**
- **Docker service scalable-microservice has a volume with container to prevent builds for every code updates**
---
# TODOS
- **Split application in different sub domain modules like: `src/app/products`**: 2 days per module
- **Use unleash for feature flag controls**: 2 days
- **Use vault to protect vulnerable secrets**: 3 days
- **Use helm charts and terraform to reuse templates and automate services deployments**: 4 days
- **Split tests module to improve CI/CD async process. Ex: `tests/unit` or `tests/integration`**: 1 day per module
- **Add a python linter like flake8 to be safe from code mistakes or best practices**: 1 day
- **Define specific versions for requirements.txt dependencies**: < 1 day
- **Move k8s folder to builder module**: < 1 day
- **Add a readiness and liveness probe for k8s monitoring**: < 1 day
- **services.get_all_data must have a redis cache to ensure read operation within 500ms to be stable in billions access scale. Look to this project as a first step** 2 days
- **Use make commands in k8s and ci file**: < 1 day
- **Add New Relic or other monitoring system**: < 1 day

---