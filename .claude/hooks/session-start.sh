#!/bin/bash
set -euo pipefail

# Only run in remote (web) environments
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Configure git credential store so pushes to GitHub work without manual auth
git config --global credential.helper store

# Ensure credentials file exists and has correct permissions
if [ ! -f ~/.git-credentials ]; then
  touch ~/.git-credentials
  chmod 600 ~/.git-credentials
fi

# Set git identity if not configured
git config --global user.email "claude-code@asistente-noticias" 2>/dev/null || true
git config --global user.name "Claude Code" 2>/dev/null || true

# Install Python backend dependencies if requirements.txt has content
REQUIREMENTS="$CLAUDE_PROJECT_DIR/backend/requirements.txt"
if [ -f "$REQUIREMENTS" ] && [ -s "$REQUIREMENTS" ]; then
  pip install -q -r "$REQUIREMENTS"
fi
