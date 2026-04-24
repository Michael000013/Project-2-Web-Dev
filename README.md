# Movie Portal - Django Web Application

A comprehensive Django web application for managing movies, trailers, news, and featured content with an admin dashboard for authorized users.

## Project Structure

```
project/
├── project/                          # Django configuration directory
│   ├── __init__.py
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # URL routing configuration
│   ├── wsgi.py                       # WSGI configuration
│   └── asgi.py                       # ASGI configuration
│
├── app/                              # Main application
│   ├── migrations/                   # Database migrations
│   │   └── __init__.py
│   ├── templates/                    # Django templates
│   │   ├── base.html                # Base template with navigation & footer
│   │   └── app/
│   │       ├── index.html            # Home page (slider + featured content)
│   │       ├── movielist.html        # Movie listing page
│   │       ├── moviedetail.html      # Individual movie details
│   │       ├── trailers.html         # Trailers page
│   │       ├── news.html             # News listing page
│   │       └── newsdetail.html       # Individual news article
│   ├── static/                       # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css            # Main stylesheet
│   │   ├── js/
│   │   │   └── custom.js            # Custom JavaScript
│   │   └── images/                   # Image assets
│   ├── __init__.py
│   ├── models.py                     # Database models
│   ├── views.py                      # View controllers
│   ├── urls.py                       # App URL routing
│   ├── admin.py                      # Admin interface configuration
│   └── apps.py                       # App configuration
│
├── manage.py                         # Django management script
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

## Database Models

### Movie
- title (CharField) - Movie title
- description (TextField) - Full description
- genre (CharField) - Movie genre
- release_date (DateField) - Release date
- cover_image (ImageField) - Movie poster
- rating (DecimalField) - IMDb-style rating (0-5)
- duration (IntegerField) - Duration in minutes
- director (CharField) - Director name
- cast (TextField) - Cast list
- Timestamps: created_at, updated_at

### Trailer
- movie (ForeignKey) - Link to Movie
- title (CharField) - Trailer title
- video_url (URLField) - YouTube URL
- thumbnail (ImageField) - Custom thumbnail
- duration (IntegerField) - Duration in seconds
- uploaded_date (DateTimeField) - Upload timestamp

### News
- title (CharField, unique) - Article title
- content (TextField) - Article content
- image (ImageField) - Featured image
- author (CharField) - Author name
- published_date (DateTimeField) - Publish date
- updated_date (DateTimeField) - Last update
- is_featured (BooleanField) - Featured status

### Slider
- title (CharField) - Slide title
- description (TextField) - Slide description
- image (ImageField) - Slide image
- link_url (URLField) - Optional link
- order (IntegerField) - Display order
- is_active (BooleanField) - Active status

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone and Navigate
```bash
cd /workspaces/Project-2-Web-Dev
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser
```bash
python manage.py createsuperuser
# Follow the prompts to create an admin account
```

### Step 6: Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`

## Usage

### Public Pages
- **Home** (`/`) - Featured content, news, and movie carousel
- **Movies** (`/movies/`) - Complete movie listing
- **Movie Detail** (`/movies/<id>/`) - Full movie information with trailers
- **Trailers** (`/trailers/`) - All available trailers
- **News** (`/news/`) - News articles and updates
- **News Detail** (`/news/<id>/`) - Full article view

### Admin Interface
- **URL**: `http://127.0.0.1:8000/admin/`
- **Access**: Login with superuser credentials created in Setup Step 5

#### Admin Features:
- **Movie Management**: Create, edit, delete movies with cover images
- **Trailer Management**: Add/edit trailers linked to movies
- **News Management**: Publish/edit news articles with featured status
- **Slider Management**: Manage hero slider images and order
- **User Management**: Create staff users with admin access

## Dynamic Content Sections

All pages use Django template tags to render dynamic database content. Sections marked with `<!-- DB -->` comments are database-driven:

### Home Page
- **Hero Slider**: Displays active slider images
- **Featured News**: Shows featured news articles
- **Recent Movies**: Lists latest movies
- **Latest News**: Shows recent news articles

### Movie List
- **Movie Cards**: Database-driven movie display
- **Pagination**: Automatic pagination for large datasets

### Movie Detail
- **Movie Info**: All movie details from database
- **Rating System**: Star rating display from database
- **Trailers**: Related trailers displayed
- **Related Movies**: Other movies in the same genre

### News List
- **Featured Articles**: Section for featured news
- **Article Cards**: Paginated news list with pagination

## Template Features

### Base Template (`base.html`)
- Navigation bar with links to all pages
- Footer with social links and quick links
- CDN links for Bootstrap 5 and Font Awesome
- Static CSS and JS file inclusion
- Template inheritance structure

### Template Inheritance
All templates extend `base.html` and override:
- `{% block title %}` - Page-specific titles
- `{% block content %}` - Main page content
- `{% block extra_css %}` - Additional styles
- `{% block extra_js %}` - Additional scripts

## Customization

### Adding CSS Styles
Edit `app/static/css/style.css` to customize:
- Color scheme (CSS variables at top)
- Component styles
- Responsive breakpoints
- Animations and transitions

### Adding JavaScript
Enhance `app/static/js/custom.js` with:
- Form validation
- User interactions
- API calls
- DOM manipulation

### Modifying Models
Edit `app/models.py` to:
- Add new fields to existing models
- Create new model classes
- Update model relationships
- Add model methods

### Extending Templates
Create new templates in `app/templates/app/` and:
- Use `{% extends 'base.html' %}`
- Override existing blocks
- Use Django template tags
- Include reusable blocks

## Admin Customization

Access Information:
Website: http://localhost:8000 (or http://127.0.0.1:8000)
Admin Panel: http://localhost:8000/admin
Username: admin
Password: admin123

Edit `app/admin.py` to:
- Add/remove list display fields
- Set up filtering options
- Configure search fields
- Customize fieldsets
- Add custom admin actions

Example:
```python
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'rating')
    list_filter = ('genre', 'rating')
    search_fields = ('title', 'director')
```

## Static Files Configuration

### Development
Static files are served automatically by Django in development mode.

### Production
Collect all static files:
```bash
python manage.py collectstatic
```

This creates a `staticfiles/` directory ready for production deployment.

## Media Files

User-uploaded images (movie covers, trailers, news images) are stored in the `media/` directory:
```
media/
├── movies/          # Movie cover images
├── trailers/        # Trailer thumbnails
├── news/            # News article images
└── slider/          # Slider images
```

## Dependencies

- **Django 4.2.0** - Web framework
- **Pillow 10.0.0** - Image processing
- **Bootstrap 5** - Frontend framework (CDN)
- **FontAwesome 6.4** - Icon library (CDN)

## Features

### Current Features
✅ Movie database with detailed information  
✅ Trailer management with YouTube integration  
✅ Entertainment news publishing  
✅ Featured content slider  
✅ Rating system for movies  
✅ Responsive mobile design  
✅ Complete admin interface  
✅ Search and filtering  
✅ Pagination support  
✅ Social sharing buttons  

### Creating Superuser
```bash
python manage.py createsuperuser
```

### Running Tests
```bash
python manage.py test
```

### Making Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Shell
```bash
python manage.py shell
```

### Database Reset (Development Only)
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

### Database Errors
```bash
python manage.py migrate
python manage.py migrate app 0001 --fake-initial
```

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

## Support & Documentation

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.0/)
- [Python Documentation](https://docs.python.org/3/)

## License

This project is provided as-is for educational purposes.

---

**Last Updated**: April 2024  
**Django Version**: 4.2.0  
**Python Version**: 3.8+