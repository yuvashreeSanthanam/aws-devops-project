# 🚀 AWS DevOps CI/CD Pipeline Project

## 📌 Project Overview

This project demonstrates a complete end-to-end DevOps CI/CD pipeline built using AWS and modern DevOps tools.

The application is a Python Flask web application that is containerized using Docker, stored in Amazon ECR, deployed to Amazon EKS using Kubernetes, and automatically deployed through GitHub Actions whenever code is pushed to the GitHub repository.

---

# 🏗️ Architecture

```
Developer
    │
    │ Git Push
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Checkout Source Code
    ├── Configure AWS Credentials
    ├── Build Docker Image
    ├── Push Image to Amazon ECR
    ├── Connect to Amazon EKS
    └── Update Kubernetes Deployment
    │
    ▼
Amazon Elastic Container Registry (ECR)
    │
    ▼
Amazon Elastic Kubernetes Service (EKS)
    │
    ▼
Kubernetes Deployment
    │
    ▼
LoadBalancer Service
    │
    ▼
Browser
```

---

# 📁 Project Structure

```
aws-devops-project
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   ├── provider.tf
│   ├── versions.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── iam.tf
│   ├── eks.tf
│   ├── nodegroup.tf
│   ├── outputs.tf
│   └── main.tf
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

- AWS
- Amazon EKS
- Amazon ECR
- Amazon VPC
- IAM
- Terraform
- Docker
- Kubernetes
- GitHub Actions
- Python
- Flask
- Git

---

# 🚀 Infrastructure Provisioned using Terraform

This project provisions the following AWS resources:

- VPC
- Public Subnets
- Internet Gateway
- Route Table
- IAM Roles
- Amazon EKS Cluster
- EKS Managed Node Group
- Amazon S3 Bucket

---

# 🐳 Docker

The Flask application is containerized using Docker.

Commands used:

```bash
docker build -t aws-devops-project .
docker tag aws-devops-project:latest <ECR_URI>:latest
docker push <ECR_URI>:latest
```

---

# ☸️ Kubernetes Deployment

Application is deployed using:

- Deployment
- LoadBalancer Service

Commands:

```bash
kubectl apply -f k8s/
kubectl get pods
kubectl get svc
```

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically performs the following steps whenever code is pushed to the **main** branch.

### CI Process

- Checkout source code
- Configure AWS credentials
- Login to Amazon ECR
- Build Docker image
- Push image to Amazon ECR

### CD Process

- Connect to Amazon EKS
- Update Deployment image
- Wait for rollout
- Verify Deployment
- Verify Pods
- Verify Services

---

# 📋 Workflow

```
Code Change
      │
      ▼
Git Commit
      │
      ▼
Git Push
      │
      ▼
GitHub Actions Triggered
      │
      ▼
Docker Image Built
      │
      ▼
Push Image to Amazon ECR
      │
      ▼
Update Amazon EKS Deployment
      │
      ▼
New Pod Created
      │
      ▼
Application Updated
```

---

# ▶️ How to Run the Project

## Clone Repository

```bash
git clone https://github.com/yuvashreeSanthanam/aws-devops-project.git
```

## Terraform

```bash
cd terraform

terraform init

terraform plan

terraform apply
```

## Configure kubectl

```bash
aws eks update-kubeconfig \
--region ap-south-1 \
--name aws-devops-cluster
```

## Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/
```

## Verify Deployment

```bash
kubectl get pods

kubectl get svc
```

---

# 📸 Screenshots

Add screenshots here:

- GitHub Actions Success
- Amazon ECR Repository
- Amazon EKS Cluster
- Running Pods
- Kubernetes Service
- Browser Output

---

# 🧪 Challenges Faced

During the implementation, the following issues were identified and resolved:

- EKS Node Group creation failure
- Unsupported EC2 instance type
- GitHub Actions configuration issues
- Docker image tagging problems
- Kubernetes Pending Pods
- EKS pod scheduling limitations
- Rolling update failures in a single-node cluster
- Kubernetes deployment strategy updates

---

# 📚 Key Learnings

- Infrastructure as Code using Terraform
- Containerization with Docker
- Kubernetes Deployments and Services
- Amazon EKS Administration
- GitHub Actions CI/CD
- Amazon ECR Image Management
- Kubernetes Troubleshooting
- End-to-End DevOps Pipeline Implementation

---

# 👨‍💻 Author

**Yuvashree Santhanam**

Cloud & DevOps Engineer

GitHub:
https://github.com/yuvashreeSanthanam