# 🎬 Movie Recommendation API

This project is a FastAPI-based backend for a Movie Recommendation System. It provides REST API endpoints that generate personalized movie recommendations based on a user's ID and viewing context.

---

# Prerequisites

Before running the project, make sure you have:

- Python 3.10 or above
- pip (Python package manager)

Install the required dependencies:

```bash
pip install -r requirements.txt
```

or install manually:

```bash
pip install fastapi uvicorn pydantic torch pandas scikit-learn
```

---

# Running the Project

Open a terminal in the project's root directory and run:

```bash
uvicorn app.main:app --reload
```

If the server starts successfully, you should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

# Accessing the API

Open your browser and navigate to:

### Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

This page provides an interactive interface where you can test all available API endpoints.

---

# Using the Recommendation Endpoint

1. Open **/docs**
2. Expand the **POST /recommend** endpoint.
3. Click **Try it out**.
4. Enter the required JSON request.
5. Click **Execute**.
6. The API will return the recommended movies in JSON format.

---

# Request Body Format

Example:

```json
{
  "user_id": 32,
  "context": 2
}
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| user_id | Unique ID of the user for whom recommendations will be generated. |
| context | Represents the viewing context (time of day). |

---

# Context Values

The `context` field only accepts the following numeric values:

| Time Context | Value |
|--------------|------:|
| Morning 🌅 | 0 |
| Evening 🌇 | 1 |
| Night 🌙 | 2 |

Example:

```json
{
  "user_id": 15,
  "context": 0
}
```

This generates recommendations for **User 15** during the **Morning**.

---

# Important Note

Only the following context values are valid:

- `0` → Morning 🌅
- `1` → Evening 🌇
- `2` → Night 🌙

Using any other value (such as `3`, `4`, etc.) is not supported and may produce incorrect results or cause an error.

---

# Example Response

```json
{
  "recommendations": [
    {
      "movie": "Inception",
      "predicted_rating": 4.92
    },
    {
      "movie": "Interstellar",
      "predicted_rating": 4.87
    },
    {
      "movie": "The Prestige",
      "predicted_rating": 4.81
    }
  ]
}
```

---

# API Workflow

```
Client
   │
   ▼
POST /recommend
   │
   ▼
FastAPI
   │
   ▼
Recommendation Service
   │
   ▼
PyTorch Model
   │
   ▼
Top Movie Recommendations
   │
   ▼
JSON Response
```

---

# Project Structure

```
app/
│
├── main.py          # FastAPI application
├── schemas.py       # Request/Response models
├── services.py      # Recommendation service
```

---

# Stopping the Server

To stop the FastAPI server, press:

```
CTRL + C
```

in the terminal where the server is running.