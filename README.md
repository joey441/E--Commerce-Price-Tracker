🛒 E-Commerce Price Tracker & Pagination Scraper
A professional, modular Python web scraper designed to track product data (Title, Price, and Availability) across multiple pages. This tool is built for reliability, using a "save-as-you-go" architecture to ensure data integrity during long scraping sessions.
🌟 Key Features
Automated Pagination: Automatically detects and navigates through "Next" page links using urllib.parse.
Modular Architecture: Separates scraping logic (scrapy.py) from data persistence (save.py) for easy maintenance and scaling.
Robust Error Handling: Uses safe extraction methods to prevent crashes if specific product elements (like price or availability) are missing on certain pages.
Data Persistence: Saves data to a structured CSV file in real-time, appending new data without overwriting previous results.
Polite Scraping: Implements randomized delays and custom User-Agent headers to respect server load and avoid IP blocks.
🛠️ Tech Stack
Python 3.x
Requests: For handling HTTP protocols and session headers.
BeautifulSoup4 (BS4): For parsing HTML and navigating the DOM using CSS selectors and Regex.
Pandas: For efficient data structuring and CSV management.
📂 Project Structure 
  ├── scrapy.py        # Core engine: handles requests, parsing, and pagination loop.
├── save.py          # Data handler: manages CSV creation and appending logic.
└── price_tracker.csv # Output: The final structured dataset (generated on first run).
 How to Use
1.Clone the repository
2.Install dependencies:
    pip install requests beautifulsoup4 pandas lxml
3.Run the scraper:
  python scrapy.py
4.Input the url   

