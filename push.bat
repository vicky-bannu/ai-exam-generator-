@echo off
echo ================================================
echo   Push to GitHub
echo ================================================
echo.
echo You need a Personal Access Token to push.
echo.
echo 1. Go to: https://github.com/settings/tokens
echo 2. Click "Generate new token (classic)"
echo 3. Select "repo" scope
echo 4. Copy the token
echo.
echo ================================================
echo.

set /p TOKEN="Enter your GitHub Personal Access Token: "

if "%TOKEN%"=="" (
    echo Error: Token is required!
    pause
    exit /b 1
)

echo.
echo Updating remote URL with token...
git remote set-url origin https://%TOKEN%@github.com/vicky-bannu/ai-exam-generator-.git

echo.
echo Pushing to GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================
    echo   Successfully pushed to GitHub!
    echo ================================================
    echo.
    echo Repository: https://github.com/vicky-bannu/ai-exam-generator-
    echo.
) else (
    echo.
    echo ================================================
    echo   Push failed!
    echo ================================================
    echo.
    echo Please check:
    echo - Token is correct
    echo - You have access to the repository
    echo - Repository exists at: https://github.com/vicky-bannu/ai-exam-generator-
    echo.
)

pause

