"""
Sample data loading script for Movie Portal

This script creates sample movies, trailers, news articles, and sliders
for testing and demonstration purposes.

Usage:
    python manage.py shell
    exec(open('load_sample_data.py').read())
"""

from datetime import datetime, timedelta
from app.models import Movie, Trailer, News, Slider

def clear_existing_data():
    """Clear existing data (optional)"""
    print("Clearing existing data...")
    Movie.objects.all().delete()
    Trailer.objects.all().delete()
    News.objects.all().delete()
    Slider.objects.all().delete()
    print("✓ Data cleared")

def load_sample_movies():
    """Load sample movie data"""
    print("\nLoading sample movies...")
    
    movies_data = [
        {
            'title': 'Inception',
            'description': 'A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea.',
            'genre': 'Sci-Fi, Thriller',
            'release_date': '2010-07-16',
            'rating': 4.8,
            'duration': 148,
            'director': 'Christopher Nolan',
            'cast': 'Leonardo DiCaprio, Ellen Page, Joseph Gordon-Levitt'
        },
        {
            'title': 'The Dark Knight',
            'description': 'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on Gotham.',
            'genre': 'Action, Crime, Drama',
            'release_date': '2008-07-18',
            'rating': 4.9,
            'duration': 152,
            'director': 'Christopher Nolan',
            'cast': 'Christian Bale, Heath Ledger, Aaron Eckhart'
        },
        {
            'title': 'Interstellar',
            'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
            'genre': 'Adventure, Drama, Sci-Fi',
            'release_date': '2014-11-07',
            'rating': 4.7,
            'duration': 169,
            'director': 'Christopher Nolan',
            'cast': 'Matthew McConaughey, Anne Hathaway, Jessica Chastain'
        },
        {
            'title': 'Parasite',
            'description': 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.',
            'genre': 'Drama, Thriller',
            'release_date': '2019-05-30',
            'rating': 4.8,
            'duration': 132,
            'director': 'Bong Joon-ho',
            'cast': 'Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong'
        },
        {
            'title': 'Everything Everywhere All at Once',
            'description': 'An aging Chinese immigrant woman is swept into an insane adventure in which only she can save the world.',
            'genre': 'Action, Adventure, Comedy',
            'release_date': '2022-11-16',
            'rating': 4.7,
            'duration': 139,
            'director': 'Daniel Kwan, Daniel Scheinert',
            'cast': 'Michelle Yeoh, Stephanie Hsu, Ke Huy Quan'
        },
    ]
    
    for movie_data in movies_data:
        movie, created = Movie.objects.get_or_create(
            title=movie_data['title'],
            defaults=movie_data
        )
        if created:
            print(f"  ✓ Created: {movie.title}")
        else:
            print(f"  • Exists: {movie.title}")
    
    print("✓ Movies loaded")
    return Movie.objects.all()

def load_sample_trailers(movies):
    """Load sample trailer data"""
    print("\nLoading sample trailers...")
    
    trailer_data = [
        {'title': 'Inception - Official Trailer', 'movie_title': 'Inception', 
         'video_url': 'https://www.youtube.com/embed/YoHD_XwrzKc', 'duration': 150},
        {'title': 'The Dark Knight - Teaser', 'movie_title': 'The Dark Knight',
         'video_url': 'https://www.youtube.com/embed/EXeTwQWrcwY', 'duration': 120},
        {'title': 'Interstellar - Official Trailer', 'movie_title': 'Interstellar',
         'video_url': 'https://www.youtube.com/embed/0vEc-3d8GkU', 'duration': 180},
    ]
    
    for trailer_info in trailer_data:
        movie = movies.filter(title=trailer_info['movie_title']).first()
        if movie:
            trailer, created = Trailer.objects.get_or_create(
                title=trailer_info['title'],
                movie=movie,
                defaults={
                    'video_url': trailer_info['video_url'],
                    'duration': trailer_info['duration']
                }
            )
            if created:
                print(f"  ✓ Created: {trailer.title}")
            else:
                print(f"  • Exists: {trailer.title}")
    
    print("✓ Trailers loaded")

def load_sample_news():
    """Load sample news data"""
    print("\nLoading sample news articles...")
    
    news_data = [
        {
            'title': 'Christopher Nolan Announces New Time-Bending Project',
            'content': 'Renowned director Christopher Nolan has announced his latest ambitious project...',
            'author': 'Jane Doe',
            'is_featured': True
        },
        {
            'title': 'Marvel Studios Confirms New Spider-Man Film',
            'content': 'Marvel Studios has officially announced the next Spider-Man film in the MCU...',
            'author': 'John Smith',
            'is_featured': True
        },
        {
            'title': 'Oscar Predictions for 2024 Released',
            'content': 'Industry experts have released their predictions for the 2024 Academy Awards...',
            'author': 'Emily Wilson',
            'is_featured': False
        },
        {
            'title': 'Upcoming Blockbusters This Summer',
            'content': 'Summer 2024 promises to be an exciting season for movie releases...',
            'author': 'Michael Brown',
            'is_featured': False
        },
    ]
    
    for news_info in news_data:
        news, created = News.objects.get_or_create(
            title=news_info['title'],
            defaults=news_info
        )
        if created:
            print(f"  ✓ Created: {news.title}")
        else:
            print(f"  • Exists: {news.title}")
    
    print("✓ News articles loaded")

def load_sample_sliders():
    """Load sample slider data"""
    print("\nLoading sample sliders...")
    
    slider_data = [
        {
            'title': 'Discover Great Movies',
            'description': 'Browse our extensive collection of films from around the world.',
            'order': 1,
            'is_active': True
        },
        {
            'title': 'Latest Trailers',
            'description': 'Watch the newest trailers from upcoming releases.',
            'order': 2,
            'is_active': True
        },
        {
            'title': 'Entertainment News',
            'description': 'Stay updated with the latest entertainment news and updates.',
            'order': 3,
            'is_active': True
        },
    ]
    
    for slider_info in slider_data:
        slider, created = Slider.objects.get_or_create(
            title=slider_info['title'],
            defaults=slider_info
        )
        if created:
            print(f"  ✓ Created: {slider.title}")
        else:
            print(f"  • Exists: {slider.title}")
    
    print("✓ Sliders loaded")

def main():
    """Main function to load all sample data"""
    print("=" * 50)
    print("Loading Movie Portal Sample Data")
    print("=" * 50)
    
    try:
        # Uncomment to clear existing data
        # clear_existing_data()
        
        movies = load_sample_movies()
        load_sample_trailers(movies)
        load_sample_news()
        load_sample_sliders()
        
        print("\n" + "=" * 50)
        print("✓ All sample data loaded successfully!")
        print("=" * 50)
        print("\nVisit http://127.0.0.1:8000 to view the portal")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
