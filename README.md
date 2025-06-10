# Python Project

This repository demonstrates a full-stack application with multiple components including backend microservices, a Next.js frontend, a React Native mobile app, edge device code, smart contracts and infrastructure as code.

## Folder Structure

```
backend/               # FastAPI microservices
frontend/              # Next.js frontend
mobile/                # React Native (Expo) mobile app
edge-devices/          # Code for edge devices
smart-contracts/       # Solidity contracts with Hardhat
infrastructure/        # Terraform modules and other IaC
functions/             # OpenFaaS functions
notebooks/             # Jupyter notebooks
openfaas.yml           # Function definitions
.github/workflows/     # CI configuration
docker-compose.yml     # Local development services
setup.sh               # Setup script
```

## Setup

1. **Start local services**
   ```bash
   ./setup.sh
   ```
   This pulls images, builds containers and launches all services via Docker Compose (databases, message queues and the three microservices).

2. **Backend services**
   ```bash
   cd backend/<service>
   pip install -r requirements.txt
   uvicorn main:app --reload --port 8000
   ```
   Each service exposes simple CRUD APIs defined using FastAPI.

3. **Frontend**
   ```bash
   cd frontend
   yarn install  # or npm install
   yarn dev
   ```

4. **Mobile**
   ```bash
   cd mobile
   yarn install  # or npm install
   expo start
   ```

5. **Smart Contracts**
   ```bash
   cd smart-contracts
   npm install
   npx hardhat test
   ```

6. **OpenFaaS Functions**
   ```bash
   faas-cli deploy -f openfaas.yml
   ```

Note: The repository does not contain a top-level `package.json`. Run npm or yarn
commands from their respective subdirectories such as `frontend`, `mobile` or
`smart-contracts`.

The CI workflow resides under `.github/workflows/ci.yml` and runs on each push to `main`.

## Edge Device Object Detection

The edge device script loads a local TorchScript model from `edge-devices/object-detection/model.pt` so it can run offline:

```python
model = torch.jit.load('model.pt')
```

Use a webcam to run detection and press `q` to quit.

## Terraform

Infrastructure modules live under `infrastructure/terraform` and can be applied using standard Terraform commands after configuring your cloud provider credentials.


## Federated Learning Example

A small PyTorch notebook under `notebooks/federated_learning.ipynb` demonstrates a simple federated averaging loop with two clients. Each round trains locally on synthetic data and then averages the model weights.

## Demo

Run `demo.py` to launch all three backend services and exercise their APIs automatically:

```bash
python demo.py
```

The script spins up the user, order and payment services using Uvicorn, creates a user, an order and a payment via HTTP and then prints the resulting lists before shutting everything down.
