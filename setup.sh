#!/bin/bash

# LMS Django Project Setup Script

echo "🔧 Setting up Django LMS Project..."

# Check Python version
echo "🐍 Checking Python version..."
python3 --version

# Install pip if not available
if ! command -v pip &> /dev/null; then
    echo "📦 Installing pip..."
    curl https://bootstrap.pypa.io/pip/3.8/get-pip.py -o get-pip.py
    python3 get-pip.py --user
    export PATH="/home/$(whoami)/.local/bin:$PATH"
fi

# Install virtualenv
echo "📦 Installing virtualenv..."
pip install --user virtualenv

# Create virtual environment
echo "🏗️ Creating virtual environment..."
virtualenv venv

# Activate virtual environment
echo "🔛 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing project dependencies..."
pip install -r requirements.txt

# Set up database
echo "🗄️ Setting up database..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "👤 Creating admin user..."
echo "from accounts.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "🚀 To start the server, run:"
echo "   ./start.sh"
echo ""
echo "📋 Admin Login Details:"
echo "   Username: admin"
echo "   Password: admin123"
echo "   Admin URL: http://127.0.0.1:8000/admin/"
echo ""
echo "🌐 Access your LMS at: http://127.0.0.1:8000"