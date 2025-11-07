from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import feedparser
from datetime import datetime

app = Flask(__name__)
CORS(app)

# News sources for Mysuru
NEWS_SOURCES = [
    {
        'name': 'Star of Mysore',
        'url': 'https://starofmysore.com',
        'rss': 'https://starofmysore.com/feed/'
    },
    {
        'name': 'Mysuru Today',
        'url': 'https://mysurutoday.com',
        'rss': 'https://mysurutoday.com/feed/'
    }
]

# Categories for services
SERVICE_CATEGORIES = [
    {
        'id': 'restaurants',
        'name': 'Restaurants & Cafes',
        'icon': '🍽️',
        'description': 'Find the best dining experiences'
    },
    {
        'id': 'hotels',
        'name': 'Hotels & Stays',
        'icon': '🏨',
        'description': 'Book comfortable accommodations'
    },
    {
        'id': 'transport',
        'name': 'Transportation',
        'icon': '🚗',
        'description': 'Get around the city easily'
    },
    {
        'id': 'attractions',
        'name': 'Tourist Attractions',
        'icon': '🏛️',
        'description': 'Explore historical sites and landmarks'
    },
    {
        'id': 'shopping',
        'name': 'Shopping',
        'icon': '🛍️',
        'description': 'Discover local markets and malls'
    },
    {
        'id': 'services',
        'name': 'Services',
        'icon': '⚙️',
        'description': 'Find essential services'
    }
]

@app.route('/')
def index():
    """Render the main landing page"""
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    """Fetch latest news from RSS feeds"""
    news_items = []
    
    for source in NEWS_SOURCES:
        try:
            # Try to parse RSS feed
            feed = feedparser.parse(source['rss'])
            
            for entry in feed.entries[:5]:  # Get top 5 items from each source
                news_items.append({
                    'title': entry.get('title', 'No title'),
                    'link': entry.get('link', '#'),
                    'description': entry.get('summary', '')[:200] + '...' if entry.get('summary') else '',
                    'published': entry.get('published', ''),
                    'source': source['name']
                })
        except Exception as e:
            print(f"Error fetching news from {source['name']}: {e}")
            # Add fallback news items
            news_items.append({
                'title': f'Latest updates from {source["name"]}',
                'link': source['url'],
                'description': 'Visit the website for the latest news and updates from Mysuru',
                'published': datetime.now().strftime('%Y-%m-%d'),
                'source': source['name']
            })
    
    # Sort by date if available
    news_items.sort(key=lambda x: x.get('published', ''), reverse=True)
    
    return jsonify(news_items[:10])  # Return top 10 news items

@app.route('/api/categories')
def get_categories():
    """Get service categories"""
    return jsonify(SERVICE_CATEGORIES)

@app.route('/api/search')
def search():
    """Search for services"""
    query = request.args.get('q', '').lower()
    category = request.args.get('category', '')
    
    # Mock search results - in production, this would query a database
    results = []
    
    if query or category:
        # Sample data for demonstration
        sample_services = [
            {
                'name': 'Mysore Palace',
                'category': 'attractions',
                'description': 'Historical palace and major tourist attraction',
                'location': 'Sayyaji Rao Road, Mysuru',
                'rating': 4.8,
                'image': 'palace.jpg'
            },
            {
                'name': 'RRR Restaurant',
                'category': 'restaurants',
                'description': 'Traditional South Indian cuisine',
                'location': 'Gandhi Square, Mysuru',
                'rating': 4.5,
                'image': 'restaurant.jpg'
            },
            {
                'name': 'Hotel Sandesh The Prince',
                'category': 'hotels',
                'description': 'Luxury hotel near city center',
                'location': 'Nazarbad Main Road, Mysuru',
                'rating': 4.3,
                'image': 'hotel.jpg'
            },
            {
                'name': 'Chamundi Hills',
                'category': 'attractions',
                'description': 'Scenic hilltop with temple',
                'location': 'Chamundi Hill Road, Mysuru',
                'rating': 4.7,
                'image': 'chamundi.jpg'
            },
            {
                'name': 'Mysore Auto Services',
                'category': 'transport',
                'description': 'Reliable auto-rickshaw services',
                'location': 'City Bus Stand, Mysuru',
                'rating': 4.2,
                'image': 'auto.jpg'
            },
            {
                'name': 'Devaraja Market',
                'category': 'shopping',
                'description': 'Traditional local market',
                'location': 'Dhanwanthri Road, Mysuru',
                'rating': 4.6,
                'image': 'market.jpg'
            }
        ]
        
        # Filter by category if specified
        if category:
            results = [s for s in sample_services if s['category'] == category]
        else:
            results = sample_services
        
        # Filter by query if specified
        if query:
            results = [s for s in results if query in s['name'].lower() or query in s['description'].lower()]
    
    return jsonify(results)

@app.route('/api/popular')
def get_popular():
    """Get popular destinations and services"""
    popular = [
        {
            'name': 'Mysore Palace',
            'category': 'attractions',
            'description': 'Iconic royal palace',
            'image': 'palace.jpg',
            'rating': 4.8
        },
        {
            'name': 'Brindavan Gardens',
            'category': 'attractions',
            'description': 'Beautiful terraced gardens',
            'image': 'brindavan.jpg',
            'rating': 4.6
        },
        {
            'name': 'Chamundi Hills',
            'category': 'attractions',
            'description': 'Sacred hill with temple',
            'image': 'chamundi.jpg',
            'rating': 4.7
        },
        {
            'name': 'Mysore Zoo',
            'category': 'attractions',
            'description': 'Well-maintained zoological garden',
            'image': 'zoo.jpg',
            'rating': 4.5
        }
    ]
    
    return jsonify(popular)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
