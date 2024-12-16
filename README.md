
# Flask Application Deployment on AWS Fargate with Docker

This project demonstrates how to containerize a simple Flask application using Docker, push the Docker image to AWS Elastic Container Registry (ECR), and then deploy the application using Amazon Elastic Container Service (ECS) with Fargate.

## Steps to Deploy

### 1. **Create a Dockerfile for the Flask Application**

A `Dockerfile` is created to containerize the Flask application. The Dockerfile includes steps to set up the application environment, install dependencies, and configure the Flask app to run on port `5000`.

### 2. **Build the Docker Image**

Once the Dockerfile is created, build the Docker image with the following command:

```bash
docker build -t flask-app .
```

### 3. **Create an ECR Repository in AWS**

- Navigate to **ECR** in the [AWS Management Console](https://aws.amazon.com/console/).
- Create a new repository in Elastic Container Registry (ECR) to store your Docker image.

### 4. **Push Docker Image to ECR**

Authenticate Docker to your AWS account and push the image:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com
docker tag flask-app:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest
docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest
```

### 5. **Create an ECS Cluster with Fargate**

- In the AWS console, go to **ECS** and create a new cluster with **Fargate** as the launch type.

### 6. **Create a Task Definition**

Create a task definition for the Flask app with the following configurations:

- Container Name: `flask-app`
- Image: `<aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest`
- Port Mappings: `5000`

### 7. **Deploy the Task to the ECS Cluster**

Deploy the task to the ECS cluster by creating a new service using the task definition and selecting **Fargate** as the launch type.

### 8. **Access the Application Using the Public IP**

Once the ECS service is running, access the application using the public IP provided by ECS (e.g., `http://<Public-IP>:5000`).


