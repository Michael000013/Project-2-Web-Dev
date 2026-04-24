# Quick Start Guide - Movie Portal Django Application

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation Steps

### 1️⃣ Clone the Repository
```bash
cd /workspaces/Project-2-Web-Dev
```

### 2️⃣ Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Admin Account
```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account:
- Username: (choose a username)
- Email: (admin email)
- Password: (choose a strong password)

### 6️⃣ (Optional) Load Sample Data
```bash
python manage.py shell
exec(open('load_sample_data.py').read())
exit()
```

### 7️⃣ Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8️⃣ Start Development Server
```bash
python manage.py runserver
```

## Accessing the Application

### 📱 Main Website
- **URL**: http://127.0.0.1:8000
- **Description**: Public-facing website

### 🔐 Admin Panel
- **URL**: http://127.0.0.1:8000/admin
- **Login**: Use superuser credentials from Step 5
- **Description**: Content management system

## Default Routes

| Page | URL | Purpose |
|------|-----|---------|
| Home | `/` | Landing page with featured content |
| Movies | `/movies/` | Movie listing |
| Movie Detail | `/movies/<id>/` | Individual movie details |
| Trailers | `/trailers/` | Movie trailers |
| News | `/news/` | News articles |
| News Detail | `/news/<id>/` | Individual article |
| Admin | `/admin/` | Admin dashboard |

## First Time Setup Checklist

- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Migrations applied
- [ ] Superuser account created
- [ ] Development server running
- [ ] Can access http://127.0.0.1:8000
- [ ] Can login to admin panel
- [ ] Sample data loaded (optional)

## Adding Content via Admin Panel

### Adding a Movie
1. Go to `/admin/`
2. Login with superuser credentials
3. Click "Movies" under "app"
4. Click "Add Movie +"
5. Fill in the form:
   - Title
   - Description
   - Genre
   - Release Date
   - Cover Image (optional)
   - Rating (0-5)
   - Duration (minutes)
   - Director
   - Cast
6. Click "Save"

### Adding a Trailer
1. Go to `/admin/`
2. Click "Trailers" under "app"
3. Click "Add Trailer +"
4. Fill in the form:
   - Movie (select from dropdown)
   - Title
   - Video URL (YouTube URL)
   - Thumbnail (optional)
   - Duration (seconds)
5. Click "Save"

### Adding News
1. Go to `/admin/`
2. Click "News" under "app"
3. Click "Add News +"
4. Fill in the form:
   - Title
   - Content
   - Image (optional)
   - Author
   - Featured (checkbox to feature)
5. Click "Save"

### Adding Slider Items
1. Go to `/admin/`
2. Click "Sliders" under "app"
3. Click "Add Slider +"
4. Fill in the form:
   - Title
   - Description
   - Image
   - Link URL (optional)
   - Order (display order)
   - Active (checkbox to show)
5. Click "Save"

## Troubleshooting

### Port 8000 Already in Use
```bash
python manage.py runserver 8001
```

### Virtual Environment Not Activating
Ensure you're in the correct directory and try:
```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### Database Locked Error
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### ModuleNotFoundError
Ensure virtual environment is activated and run:
```bash
pip install -r requirements.txt
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

## Common Commands

```bash
# Start development server
python manage.py runserver

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run Django shell
python manage.py shell

# Access specific app
python manage.py shell < load_sample_data.py

# Collect static files
python manage.py collectstatic

# Test the application
python manage.py test

# Show all available commands
python manage.py help
```

## File Structure Overview

```
Project-2-Web-Dev/
├── project/              # Django configuration
├── app/                  # Main application
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   │   ├── base.html    # Base template
│   │   └── app/         # App-specific templates
│   ├── static/          # CSS, JS, images
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin configuration
│   └── apps.py          # App config
├── manage.py            # Django management
├── requirements.txt     # Python dependencies
├── README.md           # Full documentation
├── .gitignore          # Git ignore rules
└── load_sample_data.py # Sample data script
```

## Environment Variables (.env)

Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
```

Edit .env with your settings:
- DEBUG settings
- Database configuration
- Email settings
- API keys
- AWS/CDN settings

## Next Steps

1. ✅ Complete the installation steps above
2. 📝 Add your first movie via the admin panel
3. 🎬 Add trailers for the movie
4. 📰 Create news articles
5. 🎪 Add slider images
6. 🎨 Customize CSS in `app/static/css/style.css`
7. 📱 Test on mobile devices
8. 🚀 Deploy to production

## Useful Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)
- [Python Documentation](https://docs.python.org/3/)
- [Pillow Documentation](https://pillow.readthedocs.io/)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the main README.md
3. Check Django official documentation
4. Check error logs in console output

---

Happy coding! 🚀
