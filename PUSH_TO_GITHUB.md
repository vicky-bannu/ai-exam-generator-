# How to Push to GitHub

## Authentication Required

You need to authenticate with GitHub to push. Here are the options:

## Option 1: Using Personal Access Token (Recommended)

1. **Create a Personal Access Token:**
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Give it a name (e.g., "ai-exam-generator")
   - Select scopes: `repo` (full control of private repositories)
   - Click "Generate token"
   - **Copy the token** (you won't see it again!)

2. **Push using the token:**
   ```bash
   git push https://YOUR_TOKEN@github.com/vicky-bannu/ai-exam-generator-.git main
   ```
   Replace `YOUR_TOKEN` with your actual token.

## Option 2: Using GitHub CLI

1. **Install GitHub CLI** (if not installed):
   - Download from: https://cli.github.com/

2. **Authenticate:**
   ```bash
   gh auth login
   ```

3. **Push:**
   ```bash
   git push -u origin main
   ```

## Option 3: Configure Git Credentials

1. **Set up credential helper:**
   ```bash
   git config --global credential.helper wincred
   ```

2. **Push (will prompt for credentials):**
   ```bash
   git push -u origin main
   ```
   - Username: `vicky-bannu`
   - Password: Use your Personal Access Token (not your GitHub password)

## Option 4: SSH (If you have SSH keys set up)

1. **Change remote to SSH:**
   ```bash
   git remote set-url origin git@github.com:vicky-bannu/ai-exam-generator-.git
   ```

2. **Push:**
   ```bash
   git push -u origin main
   ```

## Quick Command (Using Token)

If you have your token ready, run:
```bash
git remote set-url origin https://YOUR_TOKEN@github.com/vicky-bannu/ai-exam-generator-.git
git push -u origin main
```

Replace `YOUR_TOKEN` with your Personal Access Token.

