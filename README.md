 FastAPI Information API

This is a simple FastAPI-based API that returns information via different endpoints.

## 📌 Features
- Lightweight and fast API using FastAPI.
- Simple GET endpoints for retrieving information.
- JSON responses.

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- `pip` (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Fredrickszn06/HNG-FASTAPI-0
   HNG_FASTAPI-0
   ```



2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

### Running the API Locally
Run the API using Uvicorn:
```bash
uvicorn main:app --reload
```
- The API will be available at `http://127.0.0.1:8000`

## 📡 API Documentation

### 1️⃣ Get Root Endpoint
**URL:** `/`  
**Method:** `GET`  
**Response:**
```json
{
  "message": "Welcome to FastAPI Information API!"
}
```

### 2️⃣ Get Information
**URL:** `/info`  
**Method:** `GET`  
**Response:**
```json
{
  "data": "This is some example information."
}
```

### Example Usage
#### cURL
```bash
curl -X GET "http://127.0.0.1:8000/info"
```
#### Python Request
```python
import requests
response = requests.get("http://127.0.0.1:8000/info")
print(response.json())
```

---

## 🔗 Related Links
For hiring Python developers, check out:  
https://hng.tech/hire/python-developers
