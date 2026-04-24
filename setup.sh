#!/bin/bash

# Movie Portal - Quick Setup Script
# This script automates the initial setup process

echo "╔════════════════════════════════════════╗"
echo "║   Movie Portal - Quick Setup          ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Check Python version
echo "🔍 Checking Python version..."
python --version | grep -q "Python 3" && echo "✓ Python 3 detected" || { echo "✗ Python 3 is required"; exit 1; }

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "🔌 Activating virtual environment..."
source venv/bin/activate || . venv/Scripts/activate
echo "✓ Virtual environment activated"

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Run migrations
echo ""
echo "🗄️  Running database migrations..."
python manage.py makemigrations
python manage.py migrate
echo "✓ Migrations completed"

# Create superuser
echo ""
echo "👤 Create admin account"
echo "Run the following command to create a superuser:"
echo "python manage.py createsuperuser"
echo ""

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput
echo "✓ Static files collected"

echo ""
echo "╔════════════════════════════════════════╗"
echo "║         Setup Complete! ✓             ║"
echo "╚════════════════════════════════════════╝"
echo ""
echo "📝 Next steps:"
echo "  1. Create admin account: python manage.py createsuperuser"
echo "  2. Start development server: python manage.py runserver"
echo "  3. Visit http://127.0.0.1:8000 in your browser"
echo "  4. Admin panel: http://127.0.0.1:8000/admin"
echo ""
