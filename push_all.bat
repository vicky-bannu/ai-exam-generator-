@echo off
echo ================================================
echo   Push All Files to GitHub
echo ================================================
echo.
echo The remote only has README.md
echo Your local has all project files
echo.
echo You need a GitHub Personal Access Token
echo.
echo Get token from: https://github.com/settings/tokens
echo.
echo ================================================
echo.

set /p TOKEN="Enter your GitHub Personal Access Token: "

if "%TOKEN%"=="" (
    echo Error: Token required!
    pause
    exit /b 1
)

echo.
echo Setting up remote with token...
git remote set-url origin https://%TOKEN%@github.com/vicky-bannu/ai-exam-generator-.git

echo.
echo Force pushing all files to GitHub...
git push -u origin main --force

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================
    echo   SUCCESS! All files pushed to GitHub!
    echo ================================================
    echo.
    echo View your repository:
    echo https://github.com/vicky-bannu/ai-exam-generator-
    echo.
    echo Refresh the page to see all your files!
    echo.
) else (
    echo.
    echo ================================================
    echo   Push failed!
    echo ================================================
    echo.
    echo Please check:
    echo - Token is correct and has 'repo' scope
    echo - You have write access to the repository
    echo.
)

pause

