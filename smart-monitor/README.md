🧠 Smart Monitor – Automated Alert Aggregator with CI/CD & Telegram Notifications
[![CI/CD Status](https://github.com/JavedKhanIO/automation-lab/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/JavedKhanIO/automation-lab/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-black?logo=githubactions)](https://github.com/features/actions)

🔍 Overview

Smart Monitor is a modular monitoring and alerting system that connects multiple components 
using Redis Pub/Sub, aggregates logs, and sends real-time alerts directly to Telegram.
It is fully containerized using Docker Compose and auto-deployed via GitHub Actions.

⚙️ Architecture

##Core Components:

- monitor-app – Monitors system metrics or custom events. Publishes alerts to Redis.

- aggregator – Subscribes to Redis alerts channel, logs alerts, and forwards them to Telegram.

- redis – Message broker enabling pub/sub communication.

- action-app – Optional CI/CD deployment & orchestration layer.

##Flow:
```
monitor-app  →  Redis (alerts channel)  →  aggregator  →  Telegram Bot
```

🚀 Local Setup (Development)
1. Clone Repository
```
git clone https://github.com/<your-username>/automation-lab.git
cd automation-lab/smart-monitor
```
2. Create .env File

Create .env in the smart-monitor/ folder:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```
3. Run Locally
```
docker compose up --build -d
```

4. Check Logs
```
docker compose logs -f aggregator
```
##Screenshot for local container run
![Smart Monitor](./smart-monitor.PNG)

✅ You should see alerts being logged and forwarded to your Telegram chat.

⚡ CI/CD Setup (GitHub Actions)

The project includes a GitHub Actions pipeline that automatically:

Builds the Docker image

Runs the entire stack using docker-compose

Loads Telegram secrets securely from GitHub

Sends Telegram notifications if triggered
##Screenshot of Gitactions
![Smart Monitor Cicd](./smart-monitor-cicd)


Steps:

Go to your GitHub repo → Settings → Secrets and variables → Actions → New Repository Secret

Add:

TELEGRAM_BOT_TOKEN

TELEGRAM_CHAT_ID

Commit and push to trigger the workflow:
```
git add .
git commit -m "Added CI/CD with Telegram alerts"
git push origin main
```
🧪 Validation

✅ Works locally using .env

✅ Works on GitHub Actions using repository secrets

✅ Sends Telegram alerts in both environments

##screenshot of telegram update
![Smart Monitor Telegram](./smart-monitor-telegram.JPG)

📁 Folder Structure
```
smart-monitor/
│
├── monitor-app/
│   ├── monitor.py
│   └── Dockerfile
│
├── aggregator/
│   ├── aggregator.py
│   └── Dockerfile
│
├── docker-compose.yml
├── .env (local only)
├── .github/workflows/ci-cd.yml
└── logs/
```
🧩 Technologies Used

- Python 3

- Redis (Pub/Sub messaging)

- Docker & Docker Compose

- GitHub Actions (CI/CD)

- Telegram Bot API

- RotatingFileHandler for structured logs

🔑 Key Learnings

- How to orchestrate multiple services using Docker Compose.

- Using Redis Pub/Sub for decoupled communication between microservices.

- Logging best practices with RotatingFileHandler.

- Automating deployment and alerts with GitHub Actions.

- Securely handling secrets for Telegram bot integration in CI/CD.

- Debugging Docker container environment variables and ensuring communication between services.

🚀 Possible Future Upgrades

- Add Web UI for real-time monitoring and metrics visualization.

- Include email or Slack notifications as alternative alert channels.

- Add dynamic threshold configuration stored in Redis or a DB.

- Implement historical alert storage for analytics and reporting.

- Add multi-environment support (dev, staging, production).

- Integrate auto-scaling or cloud deployment using AWS/GCP.


📝 Author

Javed Khan
