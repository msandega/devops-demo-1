<h1>DevOps Demo App </h1>


A minimal Flask web application containerized with Docker and deployed via GitHub Actions CI/CD to Render.

<h2>**Features**</h2>

<h3>Simple Flask app with two routes:</h3>
 <ul>
   <li>/ → Returns a greeting message.</li>
  <li>/health → Returns { "status": "ok" }.</li>
  </ul>

<h3>Dockerized for portability.</h3>
GitHub Actions CI/CD:
 <ul><li> Linting with Ruff</li>
 <li> Security checks with Bandit</li>
 <li> Unit tests with Pytest</li>
 <li> Dockerfile linting with Hadolint</li>
 <li> Build & push Docker image → GHCR</li>
 <li> Auto-deploy to Render</li>
 </ul>

<h2>**Tech Stack**</h2>

<ul><li>Flask (Python)</li>
<li>Docker</li>
<li>GitHub Actions (CI/CD)</li>
<li>Render (hosting)</li></ul>

<h2>**Deployment**</h2>

Live app: (https://devops-demo-1-vcmm.onrender.com/health)



Health check: (https://devops-demo-1-vcmm.onrender.com/health)



![CI](https://github.com/msandega/devops-demo-1/actions/workflows/ci.yml/badge.svg)
![CD](https://github.com/msandega/devops-demo-1/actions/workflows/cd.yml/badge.svg)
