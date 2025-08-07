#!/bin/bash

# LMS Django Project Start Script

echo "🚀 Starting Django LMS..."

# Activate virtual environment
source venv/bin/activate

# Check if migrations are needed
echo "🔄 Checking for database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Start the development server
echo "🌐 Starting Django development server on http://127.0.0.1:8000"
echo ""
echo "📋 Admin Login Details:"
echo "   Username: admin"
echo "   Password: admin123"
echo "   Admin URL: http://127.0.0.1:8000/admin/"
echo ""
echo "🎨 Your modern LMS is ready with:"
echo "   ✨ Beautiful light color scheme"
echo "   🎯 Eye-catching dashboard"
echo "   🏗️ Modern UI components"
echo "   📱 Responsive design"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver 0.0.0.0:8000