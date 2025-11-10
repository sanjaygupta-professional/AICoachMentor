# Anand's Monday Reflections Timeline

A beautiful, interactive timeline showcasing Anand's weekly Monday posts from the Yayati Coaches WhatsApp group.

## Overview

This project extracts and displays 248 Monday posts from Anand (Anant Krishnan) spanning from 2017 to 2025. The posts are presented in an elegant, filterable timeline format that makes it easy to explore years of wisdom and life insights.

**Two versions available:**
- 🖥️ **Desktop Timeline** (`index.html`) - Full-featured web interface for desktop browsing
- 📱 **Mobile App** (`mobile.html`) - Progressive Web App with offline support and highlighting features

## Features

### Desktop Version (index.html)
- **Interactive Timeline**: Beautiful vertical timeline with chronological organization
- **Year Filtering**: Filter posts by specific years or view all at once
- **Search Functionality**: Search through all posts to find specific content
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Gradient backgrounds, smooth animations, and intuitive navigation
- **Post Statistics**: View total posts, years covered, and posts per year

### Mobile App (mobile.html) - NEW! 📱
- **⭐ Highlight Posts**: Star your favorite posts for quick access later
- **📲 Installable**: Add to home screen like a native app
- **🔌 Offline Support**: Access posts without internet connection
- **📤 Share Posts**: Native sharing to WhatsApp, social media, etc.
- **🎲 Random Wisdom**: Get random inspirational posts
- **💾 Local Storage**: Your highlights persist across sessions
- **👆 Touch-Optimized**: Smooth mobile interactions and gestures

👉 **See [MOBILE_README.md](MOBILE_README.md) for complete mobile app documentation**

## Files

### Core Files
- `index.html` - Desktop timeline webpage
- `mobile.html` - Mobile Progressive Web App (NEW!)
- `anand_posts.json` - Extracted Monday posts data (248 posts)
- `parse_anand_posts.py` - Python script to parse WhatsApp chat and extract Monday posts
- `WhatsApp Chat with Yayati Coaches.txt` - Original WhatsApp chat export

### Mobile App Files (NEW!)
- `manifest.json` - PWA configuration for installable app
- `sw.js` - Service worker for offline support
- `icon-*.png` - App icons (72px to 512px)
- `generate_icons.py` - Script to generate app icons
- `MOBILE_README.md` - Complete mobile app documentation

## How to View

### Desktop Timeline
**Option 1: Direct File Opening**
Simply open `index.html` in any modern web browser.

**Option 2: Local Web Server**
For best results, serve via a local web server:

```bash
# Using Python 3
python3 -m http.server 8000

# Desktop: http://localhost:8000/index.html
# Mobile: http://localhost:8000/mobile.html
```

### Mobile App 📱
1. Serve via local web server (see above)
2. Open `mobile.html` on your mobile device
3. Tap "Install" to add to home screen
4. Enjoy offline access and highlighting features!

**Full mobile app guide**: See [MOBILE_README.md](MOBILE_README.md)

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