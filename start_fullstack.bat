@echo off
TITLE Missing Person AI - Full-Stack Launcher
set "ROOT=%~dp0"
set "BACKEND_DIR=%ROOT%backend"
set "BACKEND_PY=%BACKEND_DIR%\.venv\Scripts\python.exe"

echo ======================================================================
echo           MISSING PERSON AI: 3-MODEL COMPARATIVE SYSTEM
echo ======================================================================
echo.

if not exist "%BACKEND_PY%" (
    echo Backend environment not found: "%BACKEND_PY%"
    echo.
    echo Create it with Python 3.12:
    echo   cd /d "%BACKEND_DIR%"
    echo   py -3.12 -m venv .venv
    echo   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo [1/2] Starting FastAPI Backend on http://127.0.0.1:8000 ...
start "Missing Person AI - Backend" /D "%BACKEND_DIR%" cmd /k ""%BACKEND_PY%" -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"

timeout /t 3 /nobreak >nul

echo [2/2] Starting Vite Frontend on http://localhost:5173 ...
start "Missing Person AI - Frontend" /D "%ROOT%frontend" cmd /k "npm run dev"

echo.
echo ======================================================================
echo Services started!
echo - Frontend Web Application: http://localhost:5173/
echo - Backend REST API Root:    http://127.0.0.1:8000/api/
echo - Interactive Swagger Docs: http://127.0.0.1:8000/docs
echo ======================================================================
echo.
pause
