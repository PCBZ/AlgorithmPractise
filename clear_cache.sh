#!/bin/bash
# Script to clear Python cache files

echo "Clearing Python cache files..."

# Remove __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

# Remove .pyc files
find . -name "*.pyc" -delete 2>/dev/null || true

# Remove .pyo files
find . -name "*.pyo" -delete 2>/dev/null || true

# Remove pytest cache
find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

# Remove coverage files
rm -f .coverage 2>/dev/null || true
rm -rf htmlcov/ 2>/dev/null || true
rm -f coverage.xml 2>/dev/null || true

echo "Cache cleared successfully!"
