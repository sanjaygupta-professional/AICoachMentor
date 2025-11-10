# Anand's Monday Reflections Timeline

A beautiful, interactive timeline showcasing Anand's weekly Monday posts from the Yayati Coaches WhatsApp group.

## Overview

This project extracts and displays 248 Monday posts from Anand (Anant Krishnan) spanning from 2017 to 2025. The posts are presented in an elegant, filterable timeline format that makes it easy to explore years of wisdom and life insights.

## Features

- **Interactive Timeline**: Beautiful vertical timeline with chronological organization
- **Year Filtering**: Filter posts by specific years or view all at once
- **Search Functionality**: Search through all posts to find specific content
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Gradient backgrounds, smooth animations, and intuitive navigation
- **Post Statistics**: View total posts, years covered, and posts per year

## Files

- `index.html` - Main timeline webpage
- `anand_posts.json` - Extracted Monday posts data (248 posts)
- `parse_anand_posts.py` - Python script to parse WhatsApp chat and extract Monday posts
- `WhatsApp Chat with Yayati Coaches.txt` - Original WhatsApp chat export

## How to View

### Option 1: Direct File Opening
Simply open `index.html` in any modern web browser.

### Option 2: Local Web Server
For best results, serve via a local web server:

```bash
# Using Python 3
python3 -m http.server 8000

# Then open: http://localhost:8000
```

## Statistics

- **Total Posts**: 248 Monday reflections
- **Time Span**: 2017-2025
- **Years Active**:
  - 2017: 1 post
  - 2018: 20 posts
  - 2021: 5 posts
  - 2022: 63 posts
  - 2023: 53 posts
  - 2024: 57 posts
  - 2025: 49 posts (ongoing)

## How It Works

1. **Parsing**: The Python script `parse_anand_posts.py` reads the WhatsApp chat export
2. **Filtering**: It identifies messages from "Anant Krishnan" posted on Mondays
3. **Organization**: Posts are organized by year and month
4. **Display**: The HTML page loads the JSON data and renders an interactive timeline

## Customization

You can easily customize the appearance by modifying the CSS variables in `index.html`:
- Color scheme (currently purple/blue gradient)
- Font styles
- Timeline layout
- Card designs

## Re-parsing Data

If you have an updated WhatsApp chat file, simply:

1. Replace the chat file
2. Run the parser:
   ```bash
   python3 parse_anand_posts.py
   ```
3. Refresh the webpage

## Credits

Created with ❤️ for the Yayati Coaches community to preserve and celebrate Anand's weekly reflections.