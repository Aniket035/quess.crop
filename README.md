# HRMS Lite – Lightweight Employee & Attendance Management

## Project Overview
A simple full-stack HR tool for admins to manage employees and daily attendance. No auth, single admin assumed.

## Tech Stack
- Frontend: React + Vite
- Backend: FastAPI (Python)
- Database: PostgreSQL (Render managed)
- Deployment: Vercel (frontend), Render (backend)

## Live URLs
- Frontend: https://aniquesscorp.vercel.app (update this after redeploy)
- Backend API: https://quess-crop.onrender.com/docs
- Full App: https://aniquesscorp.vercel.app (connected to live backend)

## Local Setup Steps
1. Backend:
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --reload

2. Frontend:
   cd frontend
   npm install
   npm run dev

## Assumptions & Limitations
- Single admin (no login system)
- Free Render Postgres expires after 30 days (data may be lost after trial)
- Backend sleeps on free tier after ~15 min inactivity → first request slow (10–60s)
- Local uses SQLite, production uses Postgres

## GitHub Repo
https://github.com/Aniket035/quess.crop
