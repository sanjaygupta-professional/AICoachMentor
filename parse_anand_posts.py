#!/usr/bin/env python3
"""
Parse WhatsApp chat to extract Anand's Monday posts
"""

import re
from datetime import datetime
from collections import defaultdict
import json

def parse_whatsapp_chat(file_path):
    """Parse WhatsApp chat file and extract messages"""
    messages = []
    current_message = None

    # Pattern: DD/MM/YYYY, HH:MM - Name: Message
    pattern = r'^(\d{1,2}/\d{1,2}/\d{4}),\s*(\d{1,2}:\d{2})\s*-\s*([^:]+):\s*(.*)$'

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                # Save previous message if exists
                if current_message:
                    messages.append(current_message)

                date_str, time_str, sender, text = match.groups()
                current_message = {
                    'date': date_str,
                    'time': time_str,
                    'sender': sender.strip(),
                    'text': text.strip()
                }
            elif current_message:
                # Continuation of previous message
                current_message['text'] += '\n' + line.strip()

        # Don't forget the last message
        if current_message:
            messages.append(current_message)

    return messages

def is_monday(date_str):
    """Check if the date string (DD/MM/YYYY) is a Monday"""
    try:
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        return date_obj.weekday() == 0  # Monday is 0
    except:
        return False

def extract_anand_monday_posts(messages):
    """Extract Monday posts from Anand"""
    anand_posts = []

    for msg in messages:
        sender = msg['sender'].lower()
        # Check for various forms of Anand's name
        if 'anant' in sender or 'anand' in sender:
            if is_monday(msg['date']):
                date_obj = datetime.strptime(msg['date'], '%d/%m/%Y')
                anand_posts.append({
                    'date': msg['date'],
                    'date_obj': date_obj,
                    'time': msg['time'],
                    'sender': msg['sender'],
                    'text': msg['text'],
                    'year': date_obj.year,
                    'month': date_obj.strftime('%B'),
                    'month_num': date_obj.month
                })

    # Sort by date
    anand_posts.sort(key=lambda x: x['date_obj'])

    return anand_posts

def organize_by_month(posts):
    """Organize posts by year and month"""
    organized = defaultdict(lambda: defaultdict(list))

    for post in posts:
        organized[post['year']][post['month']].append(post)

    return organized

def main():
    chat_file = '/home/user/AICoachMentor/WhatsApp Chat with Yayati Coaches.txt'

    print("Parsing WhatsApp chat...")
    messages = parse_whatsapp_chat(chat_file)
    print(f"Total messages parsed: {len(messages)}")

    print("\nExtracting Anand's Monday posts...")
    anand_posts = extract_anand_monday_posts(messages)
    print(f"Found {len(anand_posts)} Monday posts from Anand")

    # Organize by month
    organized_posts = organize_by_month(anand_posts)

    # Save to JSON for the webpage
    posts_data = []
    for post in anand_posts:
        posts_data.append({
            'date': post['date'],
            'time': post['time'],
            'sender': post['sender'],
            'text': post['text'],
            'year': post['year'],
            'month': post['month'],
            'month_num': post['month_num']
        })

    with open('/home/user/AICoachMentor/anand_posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts_data, f, indent=2, ensure_ascii=False)

    print("\nSample posts:")
    for i, post in enumerate(anand_posts[:5]):
        print(f"\n=== Post {i+1} ===")
        print(f"Date: {post['date']} ({post['month']} {post['year']})")
        print(f"Text: {post['text'][:200]}...")

    print(f"\n✓ Data saved to anand_posts.json")

    # Print summary by year
    print("\n=== Summary by Year ===")
    for year in sorted(organized_posts.keys()):
        total = sum(len(posts) for posts in organized_posts[year].values())
        print(f"{year}: {total} posts")
        for month in ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']:
            if month in organized_posts[year]:
                print(f"  - {month}: {len(organized_posts[year][month])} posts")

if __name__ == '__main__':
    main()
