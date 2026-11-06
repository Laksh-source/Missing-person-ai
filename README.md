
## ⚡ Quick Start Guide

### Option A: 1-Click Launcher (Windows)
After completing the backend and frontend setup below, run [`start_fullstack.bat`](./start_fullstack.bat) to start FastAPI and Vite.

### Option B: Manual Startup

#### 1. Backend Server (FastAPI)
Use Python 3.12. Python 3.14 is not supported by the TensorFlow version in the backend requirements.

```bat
cd backend
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
copy .env.example .env
REM Edit .env and set MPP_ORIGINAL_ROOT to the directory containing the original data/ and models/ folders.
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

#### 2. Frontend Application (React + Vite)
In a second terminal:
```bat
cd frontend
npm install
npm run dev
```

- **Frontend URL**: `http://localhost:5173/`
- **Backend API Root**: `http://127.0.0.1:8000/api/`
- **Swagger API Docs**: `http://127.0.0.1:8000/docs`
- **Health Check**: `http://127.0.0.1:8000/healthz`

MongoDB must be running at the `MONGODB_URL` configured in `backend/.env`.
The original AI model/data artifacts are not included in this checkout;
the API can start without them, but recognition remains unavailable until
`MPP_ORIGINAL_ROOT` points to those artifacts.

---

## 👤 Accounts & Roles

The active FastAPI backend does not seed demo users. Register through
`POST /api/auth/register`; police accounts require admin approval before
protected recognition operations. The older Django prototype is kept
separately under `legacy_backend_django/`.

---

## 🧠 3-Model AI Comparative Engine

1. **ArcFace Buffalo_L (Deep Angular Margin)**:
   - 512-dimensional normalized face embeddings with cosine similarity.
   - Best-in-class invariance to lighting, angle, and slight age variation.
2. **Deep Face CNN (Convolutional Feature Extractor)**:
   - 128-dimensional dense structural embedding for robust facial morphology.
3. **MediaPipe Facial Mesh (478-Point 3D Geometry)**:
   - 3D spatial keypoint cloud mapping landmarks across eyes, nose bridge, jawline, and mouth geometry.
4. **Consensus Aggregator**:
   - Computes normalized confidence percentages across all models, generating consensus verdicts (`MATCH FOUND`, `POSSIBLE MATCH`, `NO MATCH`).

---

## 📡 REST API Blueprint

- `POST /api/auth/register` and `POST /api/auth/login`: Create an account and obtain a JWT.
- `GET /api/persons/` and `POST /api/persons/`: List or register missing-person records.
- `POST /api/images/persons/{id}`: Upload reference photos for a person.
- `GET /api/recognition/availability`: Check which original AI models are available.
- `POST /api/recognition/search`: Search with a photo using `cnn`, `arcface`, `mediapipe_knn`, or `all`.
- `GET /api/search-history/`: Review recognition search history.

---

## 🧪 Automated Integration Tests
To run the automated backend verification suite:
```bat
cd backend
.\.venv\Scripts\python.exe -m pytest tests/ -q
```
=======
# Missing-person-ai
This project is an AI-powered platform designed to help identify and track missing persons using facial recognition
>>>>>>> bb27042abf322a6ad452f4e47a07f8077f7c3092
