#Website Health-Check API
![GitHub repo](https://img.shields.io/badge/GitHub-Repo-black?logo=github)
![License](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/JavedKhanIO/automation-lab/actions/workflows/multi-app-demo-ci-cd.yml/badge.svg)
![Docker Image](https://img.shields.io/badge/Docker-Image-blue?logo=docker)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)

📘 **Description**

This project demonstrates a lightweight Website Health Monitoring API built with Python and Flask,
containerized using Docker and automated with a scoped GitHub Actions CI pipeline.

It simulates a real-world scenario where a service periodically checks the availability and response
latency of external websites and exposes the results through a REST API endpoint.

---

## 🧰 Tools & Technologies

- Python 3
- Flask
- Requests
- Docker
- GitHub Actions
- Linux (Ubuntu)

---

## ⚙️ Architecture Overview

```text
practice/webhealth/
│
├── app.py
├── Dockerfile
├── README.md
├── output/
│   ├── output-local.PNG
│   └── output-remote.PNG
└── .github/workflows/
    └── webhealth-ci.yml
```

---

## 🔍 API Functionality

The API checks a predefined list of websites.

For each URL, it:
- Sends an HTTP request
- Measures response latency
- Determines availability status
- Returns structured JSON output

---

## 🚀 How to Run Locally

### Run without Docker

```bash
pip install flask requests
python app.py
```

Access the API:
```
http://localhost:5000/status
```

---

### Run with Docker

```bash
docker build -t website-health-api .
docker run -p 5000:5000 website-health-api
```

---

## 📊 API Output Preview

```json
[
  {
    "url": "https://www.google.com",
    "status": 200,
    "latency": 0.21,
    "up": true
  }
]
```

---

## 📸 Screenshots

### Local curl Output
![Local Output](./output-local.PNG)

### Browser Output
![Browser Output](./output-remote.PNG)

---

## 🤖 CI/CD Automation (GitHub Actions)

This project uses a scoped CI pipeline with GitHub Actions.

**Workflow file:**  
`.github/workflows/webhealth-ci.yml`

### Pipeline Stages

- **Trigger**: Runs only when files inside `practice/webhealth/` change
- **Checkout**: Fetches repository code
- **Validate**: Performs Python syntax checks
- **Build**: Builds Docker image
- **Run**: Starts container and waits for service readiness
- **Test**: Validates API endpoint using `curl`
- **Cleanup**: Stops and removes containers after execution

---

## 🧩 Output Summary

- ✅ External websites are checked for availability
- ✅ Latency is measured and returned in JSON format
- ✅ API runs consistently via Docker
- ✅ CI pipeline validates build and endpoint automatically
- ✅ Containers are cleaned up after CI execution

---

## 💡 Future Enhancements

- Make target URLs configurable via environment variables
- Add scheduled health checks and historical logging
- Integrate alerting (Slack / Telegram) on failures
- Extend CI to include automated unit tests

---

## 👤 Author

**Javed Khan**  
DevOps / Cloud Engineering Learner

- GitHub: https://github.com/JavedKhanIO  
- LinkedIn: https://www.linkedin.com/in/javedkhanio  
- Live Resume: https://javedkhanio.github.io/resume/
