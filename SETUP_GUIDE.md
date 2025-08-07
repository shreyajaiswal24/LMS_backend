# 🎓 Django LMS - Setup & Run Guide

## ✅ **Installation Complete!**

Your Django Learning Management System is now set up with a beautiful modern UI and all dependencies installed.

## 🚀 **Quick Start**

### **Option 1: Use the Start Script (Recommended)**
```bash
cd /home/shreya_24/LMS_frontend/lms-backend
./start.sh
```

### **Option 2: Manual Start**
```bash
cd /home/shreya_24/LMS_frontend/lms-backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

## 🌐 **Access Your LMS**

- **Main Website**: http://127.0.0.1:8000/ or http://localhost:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 👤 **Default Login Credentials**

```
Username: admin
Password: admin123
Email: admin@example.com
```

## 🎨 **What's New - Modern UI Features**

Your LMS now includes:

### **🌟 Visual Enhancements**
- ✨ **Modern Light Color Scheme**: Beautiful gradients with purple/blue primary colors
- 🎯 **Eye-Catching Dashboard**: Glass morphism cards with hover animations
- 🏗️ **Enhanced Navigation**: Animated sidebar with gradient backgrounds
- 📱 **Improved Responsiveness**: Better mobile and tablet experience

### **🎪 **Interactive Elements**
- 🔘 **Modern Buttons**: Gradient backgrounds with lift animations
- 🃏 **Enhanced Cards**: Semi-transparent backgrounds with blur effects
- 📊 **Beautiful Tables**: Rounded corners and improved spacing
- 🖼️ **Better Avatars**: Enhanced profile pictures with hover effects

### **🎭 **User Experience**
- ⚡ **Smooth Animations**: Micro-interactions throughout the interface
- 🌈 **Consistent Design**: Unified color system and spacing
- 👁️ **Better Hierarchy**: Clear visual organization of content
- 📖 **Enhanced Readability**: Improved contrast and typography

## 📂 **Project Structure**

```
LMS_frontend/lms-backend/
├── accounts/          # User management
├── core/             # Main app (dashboard, news)
├── course/           # Course management
├── quiz/             # Quiz system
├── result/           # Results & grades
├── payments/         # Payment integration
├── static/           # CSS, JS, images
├── templates/        # HTML templates
├── venv/             # Virtual environment
├── .env              # Environment variables
├── start.sh          # Quick start script
└── setup.sh          # Installation script
```

## ⚙️ **Configuration**

### **Environment Variables (.env)**
The following variables are configured:

```env
DEBUG=True                    # Development mode
SECRET_KEY=...               # Django secret key
EMAIL_HOST_USER=...          # Email configuration
STRIPE_SECRET_KEY=...        # Payment gateway (optional)
STUDENT_ID_PREFIX=trn        # ID prefixes
LECTURER_ID_PREFIX=inst
```

## 📦 **Dependencies Installed**

### **Core Dependencies**
- **Django 4.0.8** - Web framework
- **Pillow** - Image processing
- **WhiteNoise** - Static file serving
- **python-decouple** - Environment management

### **UI & Forms**
- **django-crispy-forms** - Form styling
- **crispy-bootstrap5** - Bootstrap 5 integration
- **django-filter** - Advanced filtering

### **Features**
- **django-modeltranslation** - Multi-language support
- **reportlab** - PDF generation
- **xhtml2pdf** - HTML to PDF conversion
- **django-jet-reboot** - Enhanced admin interface
- **stripe** - Payment processing

## 🛠️ **Common Commands**

```bash
# Activate virtual environment
source venv/bin/activate

# Start development server
python manage.py runserver 0.0.0.0:8000

# Make database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Access Django shell
python manage.py shell
```

## 🌍 **Production Deployment**

For production deployment:

1. **Install production dependencies**:
   ```bash
   pip install -r requirements/production.txt
   ```

2. **Update environment variables**:
   ```env
   DEBUG=False
   ALLOWED_HOSTS=your-domain.com
   ```

3. **Use Gunicorn**:
   ```bash
   gunicorn config.wsgi:application --bind 0.0.0.0:8000
   ```

## 🐛 **Troubleshooting**

### **Common Issues**

1. **Port already in use**:
   ```bash
   python manage.py runserver 0.0.0.0:8001
   ```

2. **Missing dependencies**:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Database errors**:
   ```bash
   python manage.py migrate
   ```

4. **Static files not loading**:
   ```bash
   python manage.py collectstatic --noinput
   ```

## 🎯 **Features Available**

- ✅ **User Management**: Students, Lecturers, Admins
- ✅ **Course Management**: Create and manage courses
- ✅ **Quiz System**: Create and take quizzes
- ✅ **Results & Grading**: Grade management
- ✅ **News & Events**: Announcements system
- ✅ **Multi-language Support**: English, Spanish, French, Russian
- ✅ **PDF Generation**: Reports and documents
- ✅ **Payment Integration**: Stripe support
- ✅ **Modern UI**: Beautiful, responsive interface

## 🎨 **Customization**

The UI has been enhanced with:
- CSS custom properties for easy color customization
- Modern gradient backgrounds
- Glass morphism effects
- Smooth animations and transitions
- Responsive design patterns

Enjoy your modern, beautiful Learning Management System! 🎉