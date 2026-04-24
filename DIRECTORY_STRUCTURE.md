# Project Directory Structure Map

## Overview
This document provides a detailed map of the Movie Portal Django project structure.

```
Project-2-Web-Dev/
│
├── 📁 project/                          # Django Configuration Directory
│   ├── __init__.py                      # Package initialization
│   ├── settings.py                      # Django settings & configuration
│   │   ├── INSTALLED_APPS              # Installed django apps
│   │   ├── MIDDLEWARE                  # Middleware configuration
│   │   ├── TEMPLATES                   # Template engine config
│   │   ├── DATABASES                   # Database configuration
│   │   └── STATIC/MEDIA FILES          # Static files config
│   │
│   ├── urls.py                          # Project URL routing
│   │   ├── admin/                       # Admin interface path
│   │   └── include('app.urls')          # Include app URLs
│   │
│   ├── wsgi.py                          # WSGI configuration for deployment
│   └── asgi.py                          # ASGI configuration for async
│
├── 📁 app/                              # Main Application Directory
│   │
│   ├── 📁 migrations/                   # Database Migrations
│   │   ├── __init__.py
│   │   └── [auto-generated migration files]
│   │
│   ├── 📁 templates/                    # HTML Templates
│   │   ├── base.html                    # Base template with layout
│   │   │   ├── Navigation bar
│   │   │   ├── Main content block
│   │   │   └── Footer
│   │   │
│   │   └── 📁 app/                      # App-specific templates
│   │       ├── index.html               # Home page with sliders & featured content
│   │       ├── movielist.html           # Movie listing page (paginated)
│   │       ├── moviedetail.html         # Single movie details
│   │       ├── trailers.html            # Trailers aggregation page
│   │       ├── news.html                # News listing page (paginated)
│   │       └── newsdetail.html          # Single news article
│   │
│   ├── 📁 static/                       # Static Files (CSS, JS, Images)
│   │   ├── 📁 css/
│   │   │   └── style.css                # Main stylesheet
│   │   │       ├── Color variables
│   │   │       ├── Navigation styles
│   │   │       ├── Card styles
│   │   │       ├── Template layout
│   │   │       └── Responsive design
│   │   │
│   │   ├── 📁 js/
│   │   │   └── custom.js                # Custom JavaScript
│   │   │       ├── DOM initialization
│   │   │       ├── User interactions
│   │   │       ├── Form validation
│   │   │       └── Utility functions
│   │   │
│   │   └── 📁 images/                   # Image assets
│   │       ├── (add logos, icons, etc.)
│   │       └── (user uploads go to media/)
│   │
│   ├── __init__.py                      # Package initialization
│   │
│   ├── models.py                        # Database Models
│   │   ├── class Movie                  # Movie model
│   │   │   ├── title (CharField)
│   │   │   ├── description (TextField)
│   │   │   ├── genre (CharField)
│   │   │   ├── release_date (DateField)
│   │   │   ├── cover_image (ImageField)
│   │   │   ├── rating (DecimalField)
│   │   │   ├── duration (IntegerField)
│   │   │   ├── director (CharField)
│   │   │   ├── cast (TextField)
│   │   │   ├── created_at (DateTimeField)
│   │   │   └── updated_at (DateTimeField)
│   │   │
│   │   ├── class Trailer                # Trailer model
│   │   │   ├── movie (ForeignKey → Movie)
│   │   │   ├── title (CharField)
│   │   │   ├── video_url (URLField)
│   │   │   ├── thumbnail (ImageField)
│   │   │   ├── duration (IntegerField)
│   │   │   └── uploaded_date (DateTimeField)
│   │   │
│   │   ├── class News                   # News model
│   │   │   ├── title (CharField, unique)
│   │   │   ├── content (TextField)
│   │   │   ├── image (ImageField)
│   │   │   ├── author (CharField)
│   │   │   ├── published_date (DateTimeField)
│   │   │   ├── updated_date (DateTimeField)
│   │   │   └── is_featured (BooleanField)
│   │   │
│   │   └── class Slider                 # Slider model
│   │       ├── title (CharField)
│   │       ├── description (TextField)
│   │       ├── image (ImageField)
│   │       ├── link_url (URLField)
│   │       ├── order (IntegerField)
│   │       ├── is_active (BooleanField)
│   │       └── created_at (DateTimeField)
│   │
│   ├── views.py                         # View Controllers
│   │   ├── class HomeView               # Home page view
│   │   ├── class MovieListView          # Movie listing view
│   │   ├── class MovieDetailView        # Movie detail view
│   │   ├── class TrailerView            # Trailers view
│   │   ├── class NewsListView           # News listing view
│   │   └── class NewsDetailView         # News detail view
│   │
│   ├── urls.py                          # App URL Routing
│   │   ├── '' → HomeView                # Home page
│   │   ├── 'movies/' → MovieListView    # Movie list
│   │   ├── 'movies/<id>/' → MovieDetailView    # Movie detail
│   │   ├── 'trailers/' → TrailerView    # Trailers
│   │   ├── 'news/' → NewsListView       # News list
│   │   └── 'news/<id>/' → NewsDetailView       # News detail
│   │
│   ├── admin.py                         # Admin Interface Configuration
│   │   ├── @admin.register(Movie)       # Movie admin
│   │   │   ├── list_display
│   │   │   ├── list_filter
│   │   │   ├── search_fields
│   │   │   └── fieldsets
│   │   │
│   │   ├── @admin.register(Trailer)     # Trailer admin
│   │   ├── @admin.register(News)        # News admin
│   │   └── @admin.register(Slider)      # Slider admin
│   │
│   └── apps.py                          # App Configuration
│       └── class AppConfig
│           └── name = 'app'
│
├── 📁 media/                            # User Uploaded Files (Auto-created)
│   ├── movies/                          # Movie cover images
│   ├── trailers/                        # Trailer thumbnails
│   ├── news/                            # News article images
│   └── slider/                          # Slider images
│
├── 📁 staticfiles/                      # Collected Static Files (Auto-created)
│   ├── css/
│   ├── js/
│   └── images/
│
├── 📄 manage.py                         # Django Management Script
│   └── Used for: python manage.py <command>
│
├── 📄 requirements.txt                  # Python Dependencies
│   ├── Django==4.2.0
│   └── Pillow==10.0.0
│
├── 📄 .gitignore                        # Git ignore rules
│   ├── Python cache
│   ├── Database files
│   ├── Media files
│   ├── Virtual environment
│   └── IDE files
│
├── 📄 .env.example                      # Environment variables template
│   ├── DEBUG setting
│   ├── SECRET_KEY
│   ├── Database config
│   ├── Email config
│   └── AWS/Storage config
│
├── 📄 setup.sh                          # Automated setup script
│   ├── Creates virtual environment
│   ├── Installs dependencies
│   ├── Runs migrations
│   └── Collects static files
│
├── 📄 load_sample_data.py               # Sample data loading script
│   ├── Creates sample movies
│   ├── Creates sample trailers
│   ├── Creates sample news
│   └── Creates sample sliders
│
├── 📄 README.md                         # Complete Project Documentation
│   ├── Project overview
│   ├── Installation steps
│   ├── Database models
│   ├── Features
│   ├── Customization guide
│   ├── Deployment instructions
│   └── Troubleshooting
│
├── 📄 QUICKSTART.md                     # Quick Start Guide
│   ├── Step-by-step installation
│   ├── Accessing application
│   ├── Adding content via admin
│   ├── Common commands
│   └── Troubleshooting
│
└── [Old files from original project]    # Legacy files
    ├── blank.html
    ├── custom.js
    ├── index.html
    ├── jquery.js
    ├── moviesingle.html
    ├── plugins.css
    ├── plugins.js
    ├── plugins2.js
    ├── slick-*.html
    └── style.css
```

## Key Files and Their Purposes

### Configuration
- `project/settings.py` - Main Django configuration
- `project/urls.py` - Project-level URL routing
- `requirements.txt` - Python package dependencies
- `.env.example` - Environment variables template

### Application Code
- `app/models.py` - Database models (Movie, Trailer, News, Slider)
- `app/views.py` - Request handlers and data display
- `app/urls.py` - App-level URL routing
- `app/admin.py` - Admin interface customization
- `app/apps.py` - App configuration

### Templates
- `app/templates/base.html` - Base template with layout
- `app/templates/app/index.html` - Home page
- `app/templates/app/movielist.html` - Movie listing
- `app/templates/app/moviedetail.html` - Movie details
- `app/templates/app/trailers.html` - Trailers page
- `app/templates/app/news.html` - News listing
- `app/templates/app/newsdetail.html` - News details

### Static Assets
- `app/static/css/style.css` - Main stylesheet
- `app/static/js/custom.js` - Custom JavaScript
- `app/static/images/` - Image assets directory

### Documentation
- `README.md` - Complete documentation
- `QUICKSTART.md` - Quick start guide
- `DIRECTORY_STRUCTURE.md` - This file

### Utilities
- `manage.py` - Django management tool
- `setup.sh` - Automated setup script
- `load_sample_data.py` - Sample data loader

## Database Structure

### Movie Table
```
id | title | description | genre | release_date | cover_image | 
rating | duration | director | cast | created_at | updated_at
```

### Trailer Table
```
id | movie_id | title | video_url | thumbnail | duration | uploaded_date
```

### News Table
```
id | title | content | image | author | published_date | 
updated_date | is_featured
```

### Slider Table
```
id | title | description | image | link_url | order | is_active | created_at
```

## URL Routing Structure

```
/
├── admin/                          # Django admin panel
│
├── (home page)                     # HomeView
│
├── movies/                         # MovieListView
│   └── <id>/                       # MovieDetailView
│
├── trailers/                       # TrailerView
│
├── news/                           # NewsListView
│   └── <id>/                       # NewsDetailView
```

## Installation Checklist

- [ ] Clone/navigate to project
- [ ] Create virtual environment
- [ ] Install dependencies (requirements.txt)
- [ ] Run migrations
- [ ] Create superuser
- [ ] Load sample data (optional)
- [ ] Collect static files
- [ ] Start development server
- [ ] Access http://127.0.0.1:8000

## File Modification Guide

### To Add a New Page:
1. Create model in `app/models.py`
2. Create view in `app/views.py`
3. Add URL in `app/urls.py`
4. Create template in `app/templates/app/`
5. Register admin in `app/admin.py`

### To Customize Styling:
1. Edit `app/static/css/style.css`
2. Use CSS variables for colors
3. Add responsive media queries

### To Add JavaScript:
1. Edit `app/static/js/custom.js`
2. Add event listeners
3. Define utility functions

### To Modify Admin:
1. Edit `app/admin.py`
2. Configure ModelAdmin classes
3. Customize list displays and filters

---

**Last Updated**: April 2024
**Version**: Django 4.2.0
**Status**: ✅ Complete and Ready for Use
