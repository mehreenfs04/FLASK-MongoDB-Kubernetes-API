# Flask MongoDB Kubernetes API

A containerized REST API built using Flask and MongoDB, deployed on Kubernetes using Docker and StatefulSets.

## Project Overview

This project demonstrates the deployment of a scalable Flask web application integrated with MongoDB in a Kubernetes environment. The application supports full CRUD (Create, Read, Update, Delete) operations through RESTful API endpoints.

MongoDB is deployed using a Kubernetes StatefulSet to ensure stable storage and persistent database management, while the Flask application is containerized using Docker and deployed through Kubernetes Deployments and Services.

## Features

- RESTful Flask API
- MongoDB database integration
- Full CRUD operations
- Docker containerization
- Kubernetes Deployment and Services
- MongoDB StatefulSet configuration
- Service discovery within Kubernetes
- Scalable application deployment

## Technologies Used

- Python
- Flask
- MongoDB
- PyMongo
- Docker
- Kubernetes
- YAML
- REST APIs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /books | Retrieve all books |
| POST | /books | Add a new book |
| GET | /books/<id> | Retrieve a specific book |
| PUT | /books/<id> | Update a book |
| DELETE | /books/<id> | Delete a book |

## Project Structure

```bash
.
├── app.py
├── Dockerfile
├── requirements.txt
├── flask-deployment.yaml
├── flask-service.yaml
├── mongodb-service.yaml
└── mongodb-statefulset.yaml
