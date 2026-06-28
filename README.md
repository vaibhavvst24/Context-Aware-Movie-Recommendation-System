# 🎬 Context Aware Movie Recommendation System

The Context-Aware Neural Recommendation Engine is an AI-powered movie recommendation system developed using PyTorch, FastAPI, and Streamlit. The system generates personalized movie recommendations by combining user preferences with contextual information such as the time of day. Unlike traditional recommendation systems that rely only on historical ratings, this project integrates contextual features to improve recommendation quality and user experience.

The project follows a modular architecture where PyTorch is used for deep learning, FastAPI provides backend API services, and Streamlit offers an interactive frontend dashboard.

---

# Live API 
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://movie-recommendation-system-4bdd.onrender.com/docs)

# Live App
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://movie-recommendation-system-dr29pjv6nyuucxuf2zhsta.streamlit.app/)

---

# 🚀 Project Overview

This project implements a Context-Aware Neural Recommendation System using a deep learning architecture with embedding layers for users and movies. The system analyzes user interaction patterns and contextual features to generate intelligent and personalized movie recommendations.

Unlike traditional recommendation systems, this project integrates:

User preferences

Movie embeddings

Contextual awareness

Neural collaborative filtering

to improve recommendation relevance and personalization.

---

# ✨ Features

✅ Context-Aware Recommendation Engine

✅ Deep Learning-based Neural Network

✅ User & Movie Embeddings using PyTorch

✅ Personalized Movie Recommendations

✅ Time-based Context Modeling

✅ Streamlit Interactive Dashboard

✅ Modern Cinematic UI Design

✅ Responsive Recommendation Cards

✅ Dockerized Deployment Support

✅ Real-world MovieLens Dataset Integration

---

# 🧠 Technologies Used

| Technology   | Purpose                  |
| :------------ | :------------------------ |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)       | **Core Programming**         |
| ![Pytorch](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=pytorch&logoColor=orange)      | **Deep Learning Model**      |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)       | **Data Processing**          |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)        | **Numerical Operations**     |
| ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) | **Encoding & Preprocessing** |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white)    | **Web Application UI**       |
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)       | **Containerized Deployment** |
| ![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge)       | **ASGI Server** |
| ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)      | **Request Validation** |
| ![Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)       | **API Documentation** |

---

# 📂 Dataset

The project uses the MovieLens Small Dataset, which contains movie ratings provided by users.

Dataset includes:

User IDs

Movie IDs

Ratings

Timestamps

Movie Titles

Genres

The timestamp information is converted into contextual categories:

Morning

Evening

Night 

---

# 🏗️ Project Architecture

User Input

   ↓

Context Feature Extraction

   ↓

Data Preprocessing

   ↓

PyTorch Embedding Layers

   ↓

Neural Recommendation Network

   ↓

Recommendation Prediction

   ↓

Streamlit Dashboard

---

# 🧠 Deep Learning Model

The recommendation engine uses:

User Embeddings

Movie Embeddings

Context Features

Fully Connected Neural Layers

---

# 🎯 Context Awareness

The system incorporates contextual information using:

Morning 🌅

Evening 🌇

Night 🌙

This improves recommendation quality by adapting recommendations based on viewing context.

---

# FastAPI Implementation

The backend exposes REST APIs that allow users to interact with the recommendation engine.

## Main Endpoint

POST /recommend

## Request Example

{
    "user_id": 25,
    "context": 1
}

## Response Example

{
   
    "recommendations": [
        {
            "movie": "The Dark Knight",
            "predicted_rating": 4.95
        },
        {
            "movie": "Inception",
            "predicted_rating": 4.90
        }
    ]
}

---

# API Testing

The API was tested using the automatically generated Swagger documentation provided by FastAPI.

Swagger UI allows developers to:

Test API endpoints

Validate request data

View JSON responses

Verify API functionality without writing additional code

---

# 🎨 UI Features

The Streamlit interface includes:

Cinematic Movie-Themed Background

Modern Recommendation Cards

Gradient Styling

Responsive Layout

Professional Footer & Header

Interactive Recommendation Display

---

# 📊 Recommendation Workflow

User enters:

User ID

Time Context

Model processes:

User embeddings

Movie embeddings

Context features

Neural network predicts:

Movie relevance score

Top recommended movies are displayed.

---

# 🔥 Future Enhancements

🎥 Movie Posters Integration

⭐ IMDb Ratings API

🔍 Movie Search Functionality

🎭 Genre-based Recommendations

🤖 Transformer-based Recommendation Model

📊 Analytics Dashboard

☁️ Cloud Deployment

🔐 User Authentication

---

## 👨‍💻 About Me

**Vaibhav Singh Bains**  
*Aspiring Data Scientist | Machine Learning Enthusiast*

- 📧 [Email](mailto:vaibhavvst8@gmail.com)
- 💼 [LinkedIn](https://www.linkedin.com/in/vaibhav-singh-bains/)
- 🐙 [GitHub](https://github.com/vaibhavvst24)

---
*Developed as a Data Science Project for Zaalima Development.*
