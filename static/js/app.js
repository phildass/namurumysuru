// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    loadCategories();
    loadPopularPlaces();
    loadNews();
    
    // Add enter key listener for search
    document.getElementById('searchInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
});

// Load service categories
async function loadCategories() {
    try {
        const response = await fetch('/api/categories');
        const categories = await response.json();
        
        const grid = document.getElementById('categoriesGrid');
        grid.innerHTML = '';
        
        categories.forEach(category => {
            const card = document.createElement('div');
            card.className = 'category-card';
            card.onclick = () => searchByCategory(category.id);
            
            card.innerHTML = `
                <div class="category-icon">${category.icon}</div>
                <h3 class="category-name">${category.name}</h3>
                <p class="category-description">${category.description}</p>
            `;
            
            grid.appendChild(card);
        });
    } catch (error) {
        console.error('Error loading categories:', error);
        document.getElementById('categoriesGrid').innerHTML = 
            '<p class="loading">Unable to load categories. Please try again later.</p>';
    }
}

// Load popular places
async function loadPopularPlaces() {
    try {
        const response = await fetch('/api/popular');
        const popular = await response.json();
        
        const grid = document.getElementById('popularGrid');
        grid.innerHTML = '';
        
        popular.forEach(place => {
            const card = document.createElement('div');
            card.className = 'popular-card';
            
            card.innerHTML = `
                <div class="popular-image">
                    🏛️
                </div>
                <div class="popular-content">
                    <span class="popular-category">${place.category}</span>
                    <h3 class="popular-title">${place.name}</h3>
                    <p class="popular-description">${place.description}</p>
                    <p class="popular-rating">⭐ ${place.rating}/5</p>
                </div>
            `;
            
            grid.appendChild(card);
        });
    } catch (error) {
        console.error('Error loading popular places:', error);
        document.getElementById('popularGrid').innerHTML = 
            '<p class="loading">Unable to load popular places. Please try again later.</p>';
    }
}

// Load news from API
async function loadNews() {
    try {
        const response = await fetch('/api/news');
        const newsItems = await response.json();
        
        const grid = document.getElementById('newsGrid');
        grid.innerHTML = '';
        
        if (newsItems.length === 0) {
            grid.innerHTML = '<p class="loading">No news items available at the moment.</p>';
            return;
        }
        
        newsItems.forEach(item => {
            const card = document.createElement('div');
            card.className = 'news-card';
            
            card.innerHTML = `
                <div class="news-source">${item.source}</div>
                <h3 class="news-title">
                    <a href="${item.link}" target="_blank" rel="noopener noreferrer">
                        ${item.title}
                    </a>
                </h3>
                <p class="news-description">${item.description}</p>
                <p class="news-date">${formatDate(item.published)}</p>
            `;
            
            grid.appendChild(card);
        });
    } catch (error) {
        console.error('Error loading news:', error);
        document.getElementById('newsGrid').innerHTML = 
            '<p class="loading">Unable to load news. Please try again later.</p>';
    }
}

// Perform search
async function performSearch() {
    const query = document.getElementById('searchInput').value.trim();
    
    if (!query) {
        alert('Please enter a search term');
        return;
    }
    
    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const results = await response.json();
        
        displaySearchResults(results, query);
    } catch (error) {
        console.error('Error performing search:', error);
        alert('Unable to perform search. Please try again later.');
    }
}

// Search by category
async function searchByCategory(categoryId) {
    try {
        const response = await fetch(`/api/search?category=${categoryId}`);
        const results = await response.json();
        
        displaySearchResults(results, `Category: ${categoryId}`);
    } catch (error) {
        console.error('Error searching by category:', error);
        alert('Unable to search. Please try again later.');
    }
}

// Display search results in modal
function displaySearchResults(results, searchTerm) {
    const modal = document.getElementById('searchModal');
    const resultsContainer = document.getElementById('searchResults');
    
    resultsContainer.innerHTML = '';
    
    if (results.length === 0) {
        const noResultsDiv = document.createElement('div');
        noResultsDiv.className = 'no-results';
        
        const heading = document.createElement('h3');
        heading.textContent = `No results found for "${searchTerm}"`;
        
        const paragraph = document.createElement('p');
        paragraph.textContent = 'Try searching with different keywords or browse our categories.';
        
        noResultsDiv.appendChild(heading);
        noResultsDiv.appendChild(paragraph);
        resultsContainer.appendChild(noResultsDiv);
    } else {
        const header = document.createElement('h3');
        header.textContent = `Found ${results.length} results for "${searchTerm}"`;
        header.style.marginBottom = '1.5rem';
        resultsContainer.appendChild(header);
        
        results.forEach(result => {
            const card = document.createElement('div');
            card.className = 'result-card';
            
            card.innerHTML = `
                <h3 class="result-title">${result.name}</h3>
                <span class="result-category">${result.category}</span>
                <p class="result-description">${result.description}</p>
                <p class="result-location">📍 ${result.location}</p>
                <p class="result-rating">⭐ ${result.rating}/5</p>
            `;
            
            resultsContainer.appendChild(card);
        });
    }
    
    modal.style.display = 'block';
}

// Close modal
function closeModal() {
    const modal = document.getElementById('searchModal');
    modal.style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('searchModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}

// Format date helper
function formatDate(dateString) {
    if (!dateString) return '';
    
    try {
        const date = new Date(dateString);
        const options = { year: 'numeric', month: 'short', day: 'numeric' };
        return date.toLocaleDateString('en-US', options);
    } catch (error) {
        return dateString;
    }
}


