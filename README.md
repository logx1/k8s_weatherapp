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


![Uploading animate k8<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 880" width="100%" height="100%" style="background-color: #0f172a; font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;">
  <defs>
    <!-- Embedded Animation Styles -->
    <style>
      /* Traffic & packet pulse flows */
      @keyframes flow-dash {
        from { stroke-dashoffset: 40; }
        to { stroke-dashoffset: 0; }
      }
      @keyframes pulse-glow {
        0%, 100% { filter: drop-shadow(0 0 2px rgba(56, 189, 248, 0.4)); opacity: 0.95; }
        50% { filter: drop-shadow(0 0 9px rgba(56, 189, 248, 0.95)); opacity: 1; }
      }
      @keyframes pulse-hpa {
        0%, 100% { stroke-opacity: 0.35; }
        50% { stroke-opacity: 1; }
      }
      @keyframes pulse-secret {
        0%, 100% { stroke-opacity: 0.4; }
        50% { stroke-opacity: 0.95; }
      }
      @keyframes badge-blink {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.35; transform: scale(0.85); }
      }
      @keyframes card-hover-fx {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-2px); }
      }

      /* Animated classes */
      .traffic-line-blue {
        stroke-dasharray: 6 6;
        animation: flow-dash 1.2s linear infinite;
      }
      .traffic-line-green {
        stroke-dasharray: 6 6;
        animation: flow-dash 1.1s linear infinite;
      }
      .traffic-line-rose {
        stroke-dasharray: 6 6;
        animation: flow-dash 0.9s linear infinite;
      }
      .traffic-line-amber {
        stroke-dasharray: 4 5;
        animation: flow-dash 2s linear infinite, pulse-secret 3s ease-in-out infinite;
      }
      .job-line {
        stroke-dasharray: 5 5;
        animation: flow-dash 1.6s linear infinite;
      }
      .hpa-border {
        animation: pulse-hpa 2.5s ease-in-out infinite;
      }
      .live-dot {
        transform-origin: center;
        animation: badge-blink 1.8s ease-in-out infinite;
      }
      .glowing-node {
        animation: pulse-glow 3s ease-in-out infinite;
      }
    </style>

    <!-- Arrow Markers -->
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#38bdf8" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#34d399" />
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#fbbf24" />
    </marker>
    <marker id="arrow-rose" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#f43f5e" />
    </marker>

    <!-- Drop Shadows -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.45"/>
    </filter>

    <!-- Gradients -->
    <linearGradient id="ingressGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#0c4a6e"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <!-- Title & Namespace -->
  <text x="40" y="46" fill="#f8fafc" font-size="22" font-weight="700" letter-spacing="0.5">Kubernetes Cluster Architecture</text>
  <rect x="40" y="60" width="168" height="26" rx="6" fill="#334155" />
  <text x="48" y="77" fill="#94a3b8" font-size="12" font-weight="500">Namespace: <tspan fill="#38bdf8" font-weight="600">default</tspan></text>
  <circle cx="218" cy="73" r="4.5" fill="#34d399" class="live-dot" />
  <text x="228" y="77" fill="#34d399" font-size="11" font-weight="600">Cluster Live</text>

  <!-- External User -->
  <g transform="translate(500, 20)">
    <rect x="0" y="0" width="180" height="42" rx="21" fill="#1e293b" stroke="#38bdf8" stroke-width="2" filter="url(#shadow)"/>
    <circle cx="24" cy="21" r="10" fill="#0284c7"/>
    <path d="M 24 17 A 3 3 0 1 0 24 23 A 3 3 0 1 0 24 17 Z M 18 27 C 18 24.5 21 23.5 24 23.5 C 27 23.5 30 24.5 30 27" stroke="#ffffff" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <text x="44" y="26" fill="#f8fafc" font-size="13" font-weight="600">External Client</text>
  </g>

  <!-- Flow: Client -> Ingress -->
  <line x1="590" y1="62" x2="590" y2="92" stroke="#38bdf8" stroke-width="2.5" class="traffic-line-blue" marker-end="url(#arrow)"/>

  <!-- Ingress -->
  <g transform="translate(435, 96)" filter="url(#shadow)" class="glowing-node">
    <rect x="0" y="0" width="310" height="66" rx="10" fill="url(#ingressGrad)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="12" y="10" width="65" height="18" rx="4" fill="#0284c7"/>
    <text x="17" y="23" fill="#ffffff" font-size="10" font-weight="700">INGRESS</text>
    <text x="85" y="24" fill="#ffffff" font-size="14" font-weight="600">weatherapp-ui-ingress</text>
    <text x="14" y="50" fill="#bae6fd" font-size="11">Class: <tspan fill="#ffffff">traefik</tspan> | Path: <tspan fill="#ffffff">/ → :3000</tspan></text>
  </g>

  <!-- Flow: Ingress -> UI Service -->
  <line x1="590" y1="162" x2="590" y2="198" stroke="#38bdf8" stroke-width="2.5" class="traffic-line-blue" marker-end="url(#arrow)"/>

  <!-- TIER 1: FRONTEND UI -->
  <g transform="translate(370, 202)" filter="url(#shadow)">
    <!-- Boundary -->
    <rect x="0" y="0" width="440" height="178" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <rect x="14" y="12" width="55" height="20" rx="4" fill="#0284c7"/>
    <text x="21" y="26" fill="#ffffff" font-size="10" font-weight="700">SERVICE</text>
    <text x="76" y="27" fill="#f8fafc" font-size="14" font-weight="600">weatherapp-ui</text>
    <text x="355" y="27" fill="#38bdf8" font-size="12" font-weight="600">Port: 3000</text>
    <line x1="14" y1="40" x2="426" y2="40" stroke="#334155" stroke-width="1"/>

    <!-- Pod Representation -->
    <g transform="translate(16, 52)">
      <rect x="0" y="0" width="408" height="66" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <rect x="10" y="10" width="76" height="18" rx="4" fill="#475569"/>
      <text x="16" y="23" fill="#ffffff" font-size="9" font-weight="700">DEPLOYMENT</text>
      <text x="94" y="24" fill="#e2e8f0" font-size="13" font-weight="600">release-name-weatherapp-ui</text>
      <text x="12" y="48" fill="#94a3b8" font-size="11">Image: <tspan fill="#e2e8f0">logx1/weatherapp-ui:v1</tspan></text>
      <rect x="306" y="40" width="90" height="18" rx="4" fill="#1e293b"/>
      <circle cx="316" cy="49" r="3.5" fill="#34d399" class="live-dot" />
      <text x="325" y="53" fill="#38bdf8" font-size="10">Replicas: 2</text>
    </g>

    <!-- HPA Badge -->
    <g transform="translate(16, 128)">
      <rect x="0" y="0" width="408" height="36" rx="6" fill="#1e293b" stroke="#0284c7" stroke-dasharray="3,3" class="hpa-border"/>
      <rect x="8" y="9" width="34" height="18" rx="3" fill="#0284c7"/>
      <text x="13" y="22" fill="#ffffff" font-size="9" font-weight="700">HPA</text>
      <text x="48" y="22" fill="#cbd5e1" font-size="11">release-name-weatherapp-ui-hpa</text>
      <text x="312" y="22" fill="#38bdf8" font-size="11" font-weight="600">min: 2 / max: 10</text>
    </g>
  </g>

  <!-- Flow Lines: UI Pod -> Backend Services -->
  <path d="M 440 380 L 440 440 L 255 440 L 255 464" fill="none" stroke="#38bdf8" stroke-width="2.5" class="traffic-line-blue" marker-end="url(#arrow)"/>
  <text x="280" y="432" fill="#94a3b8" font-size="11">http://weatherapp-auth-svc:8080</text>

  <path d="M 740 380 L 740 440 L 925 440 L 925 464" fill="none" stroke="#38bdf8" stroke-width="2.5" class="traffic-line-blue" marker-end="url(#arrow)"/>
  <text x="755" y="432" fill="#94a3b8" font-size="11">http://weatherapp-weather:5000</text>

  <!-- TIER 2 (LEFT): AUTH SERVICE -->
  <g transform="translate(60, 468)" filter="url(#shadow)">
    <rect x="0" y="0" width="390" height="178" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <rect x="14" y="12" width="55" height="20" rx="4" fill="#0284c7"/>
    <text x="21" y="26" fill="#ffffff" font-size="10" font-weight="700">SERVICE</text>
    <text x="76" y="27" fill="#f8fafc" font-size="14" font-weight="600">weatherapp-auth-svc</text>
    <text x="310" y="27" fill="#38bdf8" font-size="12" font-weight="600">Port: 8080</text>
    <line x1="14" y1="40" x2="376" y2="40" stroke="#334155" stroke-width="1"/>

    <!-- Pod Representation -->
    <g transform="translate(16, 52)">
      <rect x="0" y="0" width="358" height="66" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <rect x="10" y="10" width="76" height="18" rx="4" fill="#475569"/>
      <text x="16" y="23" fill="#ffffff" font-size="9" font-weight="700">DEPLOYMENT</text>
      <text x="94" y="24" fill="#e2e8f0" font-size="13" font-weight="600">weatherapp-auth</text>
      <text x="12" y="48" fill="#94a3b8" font-size="11">Image: <tspan fill="#e2e8f0">logx1/weatherapp-auth:v1</tspan></text>
      <rect x="256" y="40" width="90" height="18" rx="4" fill="#1e293b"/>
      <circle cx="266" cy="49" r="3.5" fill="#34d399" class="live-dot" />
      <text x="275" y="53" fill="#38bdf8" font-size="10">Replicas: 2</text>
    </g>

    <!-- HPA Badge -->
    <g transform="translate(16, 128)">
      <rect x="0" y="0" width="358" height="36" rx="6" fill="#1e293b" stroke="#0284c7" stroke-dasharray="3,3" class="hpa-border"/>
      <rect x="8" y="9" width="34" height="18" rx="3" fill="#0284c7"/>
      <text x="13" y="22" fill="#ffffff" font-size="9" font-weight="700">HPA</text>
      <text x="48" y="22" fill="#cbd5e1" font-size="11">weatherapp-auth-hpa</text>
      <text x="262" y="22" fill="#38bdf8" font-size="11" font-weight="600">min: 2 / max: 10</text>
    </g>
  </g>

  <!-- TIER 2 (RIGHT): WEATHER SERVICE -->
  <g transform="translate(730, 468)" filter="url(#shadow)">
    <rect x="0" y="0" width="390" height="178" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.5"/>
    <rect x="14" y="12" width="55" height="20" rx="4" fill="#0284c7"/>
    <text x="21" y="26" fill="#ffffff" font-size="10" font-weight="700">SERVICE</text>
    <text x="76" y="27" fill="#f8fafc" font-size="14" font-weight="600">weatherapp-weather</text>
    <text x="310" y="27" fill="#38bdf8" font-size="12" font-weight="600">Port: 5000</text>
    <line x1="14" y1="40" x2="376" y2="40" stroke="#334155" stroke-width="1"/>

    <!-- Pod Representation -->
    <g transform="translate(16, 52)">
      <rect x="0" y="0" width="358" height="66" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1"/>
      <rect x="10" y="10" width="76" height="18" rx="4" fill="#475569"/>
      <text x="16" y="23" fill="#ffffff" font-size="9" font-weight="700">DEPLOYMENT</text>
      <text x="94" y="24" fill="#e2e8f0" font-size="13" font-weight="600">weatherapp-weather</text>
      <text x="12" y="48" fill="#94a3b8" font-size="11">Image: <tspan fill="#e2e8f0">logx1/weatherapp:v2</tspan></text>
      <rect x="256" y="40" width="90" height="18" rx="4" fill="#1e293b"/>
      <circle cx="266" cy="49" r="3.5" fill="#34d399" class="live-dot" />
      <text x="275" y="53" fill="#38bdf8" font-size="10">Replicas: 2</text>
    </g>

    <!-- HPA Badge -->
    <g transform="translate(16, 128)">
      <rect x="0" y="0" width="358" height="36" rx="6" fill="#1e293b" stroke="#0284c7" stroke-dasharray="3,3" class="hpa-border"/>
      <rect x="8" y="9" width="34" height="18" rx="3" fill="#0284c7"/>
      <text x="13" y="22" fill="#ffffff" font-size="9" font-weight="700">HPA</text>
      <text x="48" y="22" fill="#cbd5e1" font-size="11">weatherapp-weather-hpa</text>
      <text x="262" y="22" fill="#38bdf8" font-size="11" font-weight="600">min: 2 / max: 10</text>
    </g>
  </g>

  <!-- Flow: Auth -> DB Service -->
  <path d="M 255 646 L 255 690 L 410 690" fill="none" stroke="#34d399" stroke-width="2.5" class="traffic-line-green" marker-end="url(#arrow-green)"/>
  <text x="265" y="682" fill="#34d399" font-size="11" font-weight="500">MySQL TCP :3306</text>

  <!-- TIER 3: DATABASE & STORAGE -->
  <g transform="translate(416, 650)" filter="url(#shadow)">
    <rect x="0" y="0" width="350" height="190" rx="12" fill="url(#cardGrad)" stroke="#059669" stroke-width="1.5"/>
    <rect x="14" y="12" width="55" height="20" rx="4" fill="#059669"/>
    <text x="21" y="26" fill="#ffffff" font-size="10" font-weight="700">SERVICE</text>
    <text x="76" y="27" fill="#f8fafc" font-size="14" font-weight="600">database-svc</text>
    <text x="270" y="27" fill="#34d399" font-size="12" font-weight="600">Port: 3306</text>
    <line x1="14" y1="40" x2="336" y2="40" stroke="#334155" stroke-width="1"/>

    <!-- Pod/StatefulSet Representation -->
    <g transform="translate(16, 50)">
      <rect x="0" y="0" width="318" height="66" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
      <rect x="10" y="10" width="80" height="18" rx="4" fill="#10b981"/>
      <text x="16" y="23" fill="#ffffff" font-size="9" font-weight="700">STATEFULSET</text>
      <text x="98" y="24" fill="#e2e8f0" font-size="13" font-weight="600">database (0/1)</text>
      <text x="12" y="48" fill="#94a3b8" font-size="11">Image: <tspan fill="#e2e8f0">mysql:5.7</tspan></text>
      <rect x="220" y="40" width="86" height="18" rx="4" fill="#1e293b"/>
      <circle cx="230" cy="49" r="3.5" fill="#34d399" class="live-dot" />
      <text x="238" y="53" fill="#34d399" font-size="10">Replicas: 1</text>
    </g>

    <!-- PVC Storage Info -->
    <g transform="translate(16, 124)">
      <rect x="0" y="0" width="318" height="52" rx="8" fill="#064e3b" stroke="#059669" stroke-width="1"/>
      <path d="M 22 14 C 22 11 34 11 34 11 C 34 11 46 11 46 14 L 46 34 C 46 37 34 37 34 37 C 34 37 22 37 22 34 Z M 22 21 C 22 24 34 24 34 24 C 34 24 46 24 46 21 M 22 28 C 22 31 34 31 34 31 C 34 31 46 31 46 28" fill="none" stroke="#6ee7b7" stroke-width="1.5"/>
      <text x="56" y="26" fill="#a7f3d0" font-size="11" font-weight="600">PVC: mysql-persistent-storage</text>
      <text x="56" y="42" fill="#d1fae5" font-size="10">10Gi | ReadWriteOnce | /var/lib/mysql</text>
    </g>
  </g>

  <!-- INIT JOB (BOTTOM LEFT) -->
  <g transform="translate(40, 716)" filter="url(#shadow)">
    <rect x="0" y="0" width="310" height="114" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.2"/>
    <rect x="12" y="10" width="32" height="18" rx="4" fill="#6366f1"/>
    <text x="17" y="23" fill="#ffffff" font-size="9" font-weight="700">JOB</text>
    <text x="50" y="24" fill="#e0e7ff" font-size="13" font-weight="600">create-mysql-user-job</text>
    <text x="14" y="48" fill="#c7d2fe" font-size="11">Waits for <tspan fill="#ffffff" font-weight="600">database-svc</tspan> ping</text>
    <text x="14" y="66" fill="#c7d2fe" font-size="11">Creates: <tspan fill="#ffffff">weatherapp</tspan> DB &amp; <tspan fill="#ffffff">'dbuser'@'%'</tspan></text>
    <rect x="12" y="78" width="130" height="22" rx="4" fill="#312e81"/>
    <circle cx="22" cy="89" r="3.5" fill="#818cf8" />
    <text x="32" y="93" fill="#a5b4fc" font-size="10">Status: Succeeded (1/1)</text>
  </g>

  <!-- Flow: Job -> DB -->
  <path d="M 350 770 L 416 770" fill="none" stroke="#818cf8" stroke-width="2" class="job-line" marker-end="url(#arrow)"/>

  <!-- CONFIG & SECRETS (FLOATING PANEL) -->
  <g transform="translate(40, 160)" filter="url(#shadow)">
    <rect x="0" y="0" width="260" height="210" rx="10" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="12" y="10" width="55" height="18" rx="4" fill="#d97706"/>
    <text x="17" y="23" fill="#ffffff" font-size="9" font-weight="700">SECRETS</text>
    <text x="74" y="24" fill="#fef3c7" font-size="13" font-weight="600">Cluster Credentials</text>
    <line x1="12" y1="36" x2="248" y2="36" stroke="#44403c" stroke-width="1"/>

    <!-- Secret: passwd -->
    <rect x="10" y="44" width="240" height="80" rx="6" fill="#292524"/>
    <text x="18" y="60" fill="#fbbf24" font-size="11" font-weight="600">Secret: passwd</text>
    <text x="18" y="76" fill="#d6d3d1" font-size="10">• AUTH-PASSWORD</text>
    <text x="18" y="92" fill="#d6d3d1" font-size="10">• MYSQL_ROOT_PASSWORD</text>
    <text x="18" y="108" fill="#d6d3d1" font-size="10">• secret-key</text>

    <!-- Secret: weather -->
    <rect x="10" y="132" width="240" height="42" rx="6" fill="#292524"/>
    <text x="18" y="148" fill="#fbbf24" font-size="11" font-weight="600">Secret: weather</text>
    <text x="18" y="164" fill="#d6d3d1" font-size="10">• apikey (external weather API)</text>

    <text x="12" y="194" fill="#78716c" font-size="9" font-style="italic">Injected as environment variables</text>
  </g>

  <!-- Secret Connection Indicators -->
  <path d="M 300 240 L 370 270" fill="none" stroke="#fbbf24" stroke-width="1.8" class="traffic-line-amber" marker-end="url(#arrow-amber)"/>
  <path d="M 200 370 L 200 468" fill="none" stroke="#fbbf24" stroke-width="1.8" class="traffic-line-amber" marker-end="url(#arrow-amber)"/>
  <path d="M 300 170 C 500 130 900 180 925 468" fill="none" stroke="#fbbf24" stroke-width="1.8" class="traffic-line-amber" marker-end="url(#arrow-amber)"/>

  <!-- EXTERNAL API (FAR RIGHT) -->
  <g transform="translate(860, 716)" filter="url(#shadow)">
    <rect x="0" y="0" width="260" height="96" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="1.2"/>
    <rect x="12" y="10" width="65" height="18" rx="4" fill="#e11d48"/>
    <text x="17" y="23" fill="#ffffff" font-size="9" font-weight="700">EXTERNAL</text>
    <text x="84" y="24" fill="#ffe4e6" font-size="13" font-weight="600">Weather API</text>
    <text x="14" y="48" fill="#f43f5e" font-size="11">RapidAPI / Third-party HTTP</text>
    <text x="14" y="66" fill="#fda4af" font-size="10">Authenticated via injected <tspan fill="#ffffff">apikey</tspan></text>
  </g>

  <!-- Flow: Weather Service -> External API -->
  <path d="M 925 646 L 925 716" fill="none" stroke="#f43f5e" stroke-width="2.5" class="traffic-line-rose" marker-end="url(#arrow-rose)"/>

  <!-- LEGEND (BOTTOM BAR) -->
  <g transform="translate(40, 846)">
    <line x1="0" y1="0" x2="30" y2="0" stroke="#38bdf8" stroke-width="2.5" class="traffic-line-blue"/>
    <text x="38" y="4" fill="#94a3b8" font-size="11">Active HTTP Route</text>

    <line x1="180" y1="0" x2="210" y2="0" stroke="#34d399" stroke-width="2.5" class="traffic-line-green"/>
    <text x="218" y="4" fill="#94a3b8" font-size="11">Active MySQL Stream</text>

    <line x1="360" y1="0" x2="390" y2="0" stroke="#fbbf24" stroke-width="1.8" class="traffic-line-amber"/>
    <text x="398" y="4" fill="#94a3b8" font-size="11">Secret Ingestion Flow</text>

    <line x1="530" y1="0" x2="560" y2="0" stroke="#f43f5e" stroke-width="2.5" class="traffic-line-rose"/>
    <text x="568" y="4" fill="#94a3b8" font-size="11">External Outbound</text>

    <line x1="700" y1="0" x2="730" y2="0" stroke="#818cf8" stroke-width="2" class="job-line"/>
    <text x="738" y="4" fill="#94a3b8" font-size="11">Job Completion Pulse</text>
  </g>
</svg>
s.svg…]()

- The **Weather Service** expects an API key to be available via a Secret named `weather` (key `apikey`).
- The **Auth Service** and **Database** expect passwords to be available via a Secret named `passwd`.
