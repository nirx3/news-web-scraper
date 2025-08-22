# News Scraper: BBC & TechCrunch

A Python-based web scraper to fetch recent articles from **BBC** and **TechCrunch** based on a user-specified keyword. The scraper counts articles published within the last **7 days**.

---

## Features

* Scrapes **BBC** and **TechCrunch** news websites.
* Filters articles by **keyword**.
* Handles **relative dates** (e.g., “2 days ago”) for BBC.
* Converts TechCrunch article timestamps to **Nepal Time (NPT, UTC+5:45)**.
* Counts articles published in the last **7 days**.
* User-friendly console interface.

---

## Requirements

* Python 3.8+
* Libraries:

  ```bash
  pip install requests beautifulsoup4
  ```

---

## Usage

1. Clone or download the repository.
2. Run the script:

   ```bash
   python news-web-scraper.py
   ```
3. Input the **keyword** when prompted:

   ```
   Keyword filter: Technology
   ```
4. The script will display:

   ```
   [✓] BBC: X articles found
   [✓] Techcrunch: Y articles found
   ```

---

## How It Works

* **BBC Scraper:**

  * Searches BBC articles using the query and page numbers.
  * Extracts article title, description, and publication date.
  * Handles dates expressed as “days ago” and converts them to standard format.

* **TechCrunch Scraper:**

  * Scrapes paginated articles using query parameters.
  * Extracts article title and ISO timestamp.
  * Converts timestamps to Nepal Time and filters articles within the last 7 days.

---

## Notes

* User input is capitalized automatically.
* Articles older than 7 days are ignored in the count.
* The script uses custom **User-Agent headers** to mimic a browser.

---

## Limitations

* No advanced error handling for network failures or HTML structure changes.
* BBC class names may change over time, which could break the scraper.
* Currently prints results to console only; no file export.

---

## Future Improvements

* Export results to **CSV or JSON**.
* Add **more news sources**.
* Use `requests.Session()` for faster repeated requests.
* Handle network errors and retries.
* Modularize scraper functions for better reuse.

---

## License

MIT License © 2025
