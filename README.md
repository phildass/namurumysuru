# Namuru Mysuru - Discover Mysuru 🏰

Your comprehensive guide to everything in Mysuru (Mysore), the City of Palaces. This web application helps tourists and locals discover services, attractions, restaurants, hotels, and more, while staying updated with the latest news from the city.

## Features

- 🔍 **Smart Search**: Find anything, anywhere in Mysuru
- 🏛️ **Service Categories**: Browse restaurants, hotels, attractions, transportation, shopping, and services
- 📰 **News Feed**: Real-time news and updates from Mysuru
- 🌟 **Popular Destinations**: Discover must-visit places
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile
- 🌐 **Web Scraping**: Aggregates information from multiple sources

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Web Scraping**: BeautifulSoup, feedparser
- **API**: RESTful API endpoints

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/phildass/namurumysuru.git
cd namurumysuru
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
namurumysuru/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── styles.css    # Styling
│   └── js/
│       └── app.js        # Frontend JavaScript
└── README.md             # This file
```

## API Endpoints

- `GET /` - Main landing page
- `GET /api/news` - Fetch latest news from Mysuru
- `GET /api/categories` - Get service categories
- `GET /api/search?q=query&category=cat` - Search for services
- `GET /api/popular` - Get popular destinations

## Features Overview

### Search Functionality
Search for any service, attraction, or business in Mysuru. The search supports:
- General keyword search
- Category-based filtering
- Real-time results

### News Aggregation
The app scrapes news from multiple Mysuru-based news sources:
- Star of Mysore
- Mysuru Today
- And more can be added easily

### Service Categories
- 🍽️ Restaurants & Cafes
- 🏨 Hotels & Stays
- 🚗 Transportation
- 🏛️ Tourist Attractions
- 🛍️ Shopping
- ⚙️ Services

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## About Mysuru

Mysuru (Mysore) is a historic city in Karnataka, India, known for:
- The magnificent Mysore Palace
- Rich cultural heritage
- Dasara festival celebrations
- Silk sarees and sandalwood products
- Beautiful gardens and temples

## License

This project is open source and available for educational and personal use.

## Contact

For questions or suggestions, please open an issue on GitHub.

---

Made with ❤️ for Mysuru
