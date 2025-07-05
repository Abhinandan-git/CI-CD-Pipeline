# CI/CD Pipeline for Full-Stack TODO Application

This project demonstrates a complete CI/CD pipeline setup for a simple full-stack TODO application. The main goal is to showcase DevOps practices using automation for building, testing, and deploying a web application.

The frontend is deployed on **Vercel**, and the backend is deployed on **Render**. GitHub Actions is used as the CI/CD tool to manage the workflow.

---

## 📌 Project Structure

- **Frontend**: React / Next.js-based TODO UI
- **Backend**: REST API built with FastAPI
- **CI/CD Tool**: GitHub Actions
- **Deployment**: 
  - Frontend: Vercel
  - Backend: Render
- **Containerization**: Docker & Docker Compose (for local development)

---

## ⚙️ Features

- Automated testing on each push
- Dockerized development and production environments
- Continuous deployment triggered via GitHub Actions
- Environment-specific configuration using `.env` files
- Auto-deploy backend to Render using Webhooks or GitHub integration
- Auto-deploy frontend to Vercel via Vercel Git Integration

---

## 🚀 CI/CD Workflow (GitHub Actions)

### Frontend

1. **Trigger**: On push to `main`
2. **Steps**:
   - Checkout code
   - Install dependencies
   - Run tests (if any)
   - Deploy to Vercel (Vercel handles this via Git integration)

### Backend

1. **Trigger**: On push to `main` or `api` folder
2. **Steps**:
   - Checkout code
   - Set up Python
   - Install dependencies from `requirements.txt`
   - Run tests using pytest
   - If tests pass, deploy to Render using GitHub integration or API

---

## 🧰 Technologies Used

| Layer      | Technology      |
|------------|------------------|
| Frontend   | React / Next.js  |
| Backend    | FastAPI          |
| CI/CD      | GitHub Actions   |
| Deployment | Vercel, Render   |
| Docker     | Docker & Compose |
| Testing    | pytest / React Testing Library |

---

## 📂 Folder Structure

```bash
ci-cd-todo-app/
├── frontend/           # Next.js/React application
│   ├── pages/
│   ├── components/
│   └── ...
├── backend/            # FastAPI application
│   ├── main.py
│   ├── authentication/
│   ├── database/
│   ├── todo/
│   └── ...
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── docker-compose.yml
└── README.md
````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/abhinandan-git/ci-cd-pipeline.git
cd ci-cd-pipeline
```

### 2. Run Locally with Docker Compose

```bash
docker-compose up --build
```

Access:

* Frontend: `http://localhost:3000`
* Backend API: `http://localhost:8000`

### 3. Configure Vercel & Render

* Connect frontend repo to Vercel via GitHub for auto-deploys
* Connect backend repo or subdirectory to Render via GitHub or use a Render blueprint with Docker
* Add environment variables via respective dashboards

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

## 🙌 Author

Built by [Abhinandan Jain](https://github.com/abhinandan-git).
Feel free to fork, contribute, or raise issues.
