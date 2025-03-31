#!/bin/bash

# Script to push the Streamlit dashboard to GitHub

# Check if the repository URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <github_repository_url>"
  echo "Example: $0 https://github.com/Lpxbt/streamlit-dashboard.git"
  exit 1
fi

REPO_URL=$1

# Add the remote repository
git remote add origin $REPO_URL

# Push to GitHub
git push -u origin main

echo "Repository pushed to $REPO_URL"
echo "Next steps:"
echo "1. Go to https://share.streamlit.io/ and sign in with your GitHub account"
echo "2. Click on \"New app\""
echo "3. Select the repository, branch (main), and file (dashboard.py)"
echo "4. Click \"Deploy\""
echo "5. Once deployed, you can access your dashboard at https://username-repository-name.streamlit.app/"
