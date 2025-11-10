#!/usr/bin/env python3
"""
Generate app icons for Anand's Monday Wisdom PWA
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("PIL not available, will create SVG icons instead")

import os

def create_icon_with_pil(size, filename):
    """Create a beautiful gradient icon with PIL"""
    # Create image with gradient background
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)

    # Create gradient background (purple to blue)
    for y in range(size):
        r = int(102 + (118 - 102) * y / size)  # 667eea to 764ba2
        g = int(126 + (75 - 126) * y / size)
        b = int(234 + (162 - 234) * y / size)
        draw.rectangle([(0, y), (size, y+1)], fill=(r, g, b))

    # Add star emoji representation (simplified)
    star_size = size // 2
    star_x = size // 2
    star_y = size // 2

    # Draw a star shape
    points = []
    for i in range(5):
        outer_angle = i * 72 - 90
        inner_angle = outer_angle + 36

        outer_x = star_x + int(star_size * 0.4 * (1 if i % 2 == 0 else 0.4) *
                               __import__('math').cos(__import__('math').radians(outer_angle)))
        outer_y = star_y + int(star_size * 0.4 * (1 if i % 2 == 0 else 0.4) *
                               __import__('math').sin(__import__('math').radians(outer_angle)))
        points.append((outer_x, outer_y))

        inner_x = star_x + int(star_size * 0.4 * 0.4 *
                               __import__('math').cos(__import__('math').radians(inner_angle)))
        inner_y = star_y + int(star_size * 0.4 * 0.4 *
                               __import__('math').sin(__import__('math').radians(inner_angle)))
        points.append((inner_x, inner_y))

    # Draw filled star
    draw.polygon(points, fill='gold', outline='white')

    # Add circle border
    border_width = max(2, size // 50)
    draw.ellipse(
        [(border_width, border_width), (size-border_width, size-border_width)],
        outline='white',
        width=border_width
    )

    # Save
    img.save(filename, 'PNG')
    print(f"Created {filename} ({size}x{size})")

def create_svg_icon(size, filename):
    """Create SVG icon as fallback"""
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="{size}" height="{size}" fill="url(#grad)"/>
  <circle cx="{size//2}" cy="{size//2}" r="{size//2-10}" fill="none" stroke="white" stroke-width="4"/>
  <text x="{size//2}" y="{size//2+size//6}" font-size="{size//2}" text-anchor="middle" fill="gold">⭐</text>
</svg>'''

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created {filename} ({size}x{size} SVG)")

def main():
    sizes = [72, 96, 128, 144, 152, 192, 384, 512]

    for size in sizes:
        filename = f'icon-{size}.png'

        if HAS_PIL:
            create_icon_with_pil(size, filename)
        else:
            # For SVG, we still name it .png but it's actually SVG
            # In production, you'd want actual PNG files
            svg_filename = f'icon-{size}.svg'
            create_svg_icon(size, svg_filename)
            print(f"Note: Created SVG instead of PNG for icon-{size}")

    print("\n✓ Icon generation complete!")
    print("\nFor production, consider:")
    print("1. Using a professional icon designer")
    print("2. Or using online tools like realfavicongenerator.net")
    print("3. Installing PIL: pip install Pillow")

if __name__ == '__main__':
    main()
