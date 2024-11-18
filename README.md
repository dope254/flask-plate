# Flask App Boilerplate

A reusable boilerplate for building Flask applications with modular structure and efficient deployment workflows.

## Features

- Modular structure (Domain, Application, Infrastructure, Presentation layers).
- Built-in Docker, Kubernetes, and Ansible configurations.
- Predefined repository and external service templates.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the app locally:

    `python main.py`

3. Build and run using Docker:

    `docker-compose up --build`

4. Deploy using Kubernetes:

    `kubectl apply -f kubernetes/`

5. Manage with Ansible:

    `ansible-playbook ansible/playbooks/sample-playbook.yml`

Structure

    Domain: Business logic and models.
    Application: Use cases and application logic.
    Infrastructure: Data persistence, API integrations.
    Presentation: Frontend/UI logic.