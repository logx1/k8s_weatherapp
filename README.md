![animate k8s](https://github.com/user-attachments/assets/85cffcf1-9fc5-4512-a478-7d48cfb45c65)# Kubernetes Weather App

This is a microservices-based weather application designed to run on Kubernetes.

## Architecture Diagram

The application consists of the following microservices:
- **UI Service**: Serves the frontend interface and acts as the main entry point for the user. (Exposed via Ingress).
- **Auth Service**: Handles user authentication, registration, and session management.
- **Weather Service**: Fetches weather data using an external API based on user requests.
- **Database**: A MySQL database used by the Auth Service to store user credentials.

Here is a diagram showing how these services interact with one another:

```mermaid
graph TD
    User([User]) -->|HTTP Request| Ingress[weatherapp-ui-ingress]
    Ingress --> UI[UI Service / weatherapp-ui]
    
    UI -->|Auth Check/Login| Auth[Auth Service / weatherapp-auth]
    UI -->|Weather Request| Weather[Weather Service / weatherapp-weather]
    
    Auth -->|Read/Write User Data| DB[(MySQL Database / database)]
    
    Weather -.->|External API Call| ExtWeatherAPI([External Weather API])
```

## Microservices Breakdown

1. **weatherapp-ui** (`logx1/weatherapp-ui:v1`)
   - Replicas: 2
   - Port: 3000
   - Dependencies: `weatherapp-auth`, `weatherapp-weather`

2. **weatherapp-auth** (`logx1/weatherapp-auth:v1`)
   - Replicas: 2
   - Port: 8080
   - Dependencies: `database-svc` (MySQL)

3. **weatherapp-weather** (`logx1/weatherapp:v2`)
   - Replicas: 2
   - Port: 5000

4. **database** (`mysql:5.7`)
   - Replicas: 1 (StatefulSet)
   - Port: 3306
   - Persistent Storage: 10Gi

## Prerequisites

- A running Kubernetes cluster.
- `kubectl` configured to interact with your cluster.
- An Ingress controller (e.g., Traefik, which is assumed by the provided ingress).

## Installation

The project uses Kustomize to manage deployments. You can deploy the entire stack using `kubectl`:

```bash
# Apply the Kustomization from the root directory
kubectl apply -k .
```

This command will apply all manifests defined in `kustomization.yaml`, including Deployments, Services, HorizontalPodAutoscalers, StatefulSets, Jobs, and Ingresses for the application components.

### Secrets Configuration

Make sure you have populated the correct Secrets for the application to work:

<img width="2816" height="1536" alt="Gemini_Generated_Image_slobvhslobvhslob" src="https://github.com/user-attachments/assets/b20aa0f0-4db0-4d17-9f65-8d0d61cce1f2" />


- The **Weather Service** expects an API key to be available via a Secret named `weather` (key `apikey`).
- The **Auth Service** and **Database** expect passwords to be available via a Secret named `passwd`.
