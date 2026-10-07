# DeployHub Django Application

A lightweight, production-ready Django REST Framework application designed for deployment validation, testing CI/CD pipelines, Docker containerization, and server deployments on DeployHub.

---

## 🚀 Features

- **Django 5.x & Python 3.11+**
- **Django REST Framework (DRF)** & **CORS Headers** configured
- **Gunicorn WSGI Server** & **Whitenoise** static asset compression
- **Multi-worker Dockerfile** (Zero host dependency needed; runs containerized)
- **Docker Compose** ready for one-command deployment
- **REST Endpoints** for health, deployment sanity checks, and greeting parameter tests

---

## 📡 API Endpoints

| Method | Endpoint | Description | Sample Output |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root deployment sanity check | `{"status":"SUCCESS","message":"Hello Deployment Test User!...","timestamp":"...","hostname":"..."}` |
| `GET` | `/api/hello?name=John` | Greeting endpoint with hostname | `{"status":"SUCCESS","message":"Hello John!...","timestamp":"...","hostname":"..."}` |
| `GET` | `/api/health` | Health check endpoint | `{"status":"UP","timestamp":"...","service":"deploy_hub_django"}` |
| `GET` | `/api/info` | Application info and routes | `{"appName":"deploy_hub_django","framework":"Django 5.x",...}` |

---

## 🐳 Docker Deployment

### 1. Run with Docker Compose (Recommended)
```bash
docker compose up -d --build
```
Check running container:
```bash
docker compose ps
docker compose logs -f
```
Stop container:
```bash
docker compose down
```

### 2. Run with Docker CLI
```bash
# Build the image
docker build -t deploy-hub-django-app:latest .

# Run the container
docker run -d -p 8000:8000 --name deploy_hub_django_container deploy-hub-django-app:latest
```

---

## 💻 Local Development (Without Docker)

Requires Python 3.10+:
```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations & start server
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

---

## 🧪 Quick Test (cURL)
```bash
curl http://localhost:8000/
curl http://localhost:8000/api/hello?name=Developer
curl http://localhost:8000/api/health
curl http://localhost:8000/api/info
```