@echo off
title AI Exam Generator
color 0B
echo.
echo ================================================
echo    AI EXAM GENERATOR
echo ================================================
echo.
echo Starting API server on http://localhost:5000
echo.
echo Predefined subjects available:
echo   - Python
echo   - Java
echo   - Machine Learning
echo   - Database
echo.
echo Opening browser...
echo.
echo Press Ctrl+C to stop the server
echo ================================================
echo.

cd /d "%~dp0"

REM Open browser
start msedge index.html

REM Wait a moment
timeout /t 2 /nobreak >nul

REM Start API server
python api_server.py

pause

