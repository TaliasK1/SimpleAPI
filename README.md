# Python API with Jenkins + Kaniko + Harbor + ArgoCD

This project exposes a basic FastAPI application with the following CI/CD pipeline:
- Build and test with Jenkins
- Build image using Kaniko
- Push to Harbor registry
- (Optional) Deploy via ArgoCD

## Endpoints
- `GET /` → Hello World
- `GET /health` → Health check
- `GET /hello/{name}` → Personalized greeting
- `POST /echo` → Echo JSON payload

## Install Requirements
```bash
pip install -r requirements.txt
```


## Run Locally
```bash
uvicorn app.main:app --reload
```



## Run Tests
```bash
pytest
```
