from PIL import Image
import os

# Use the logo source file
logo_path = 'assets/c42bcc64-85a7-47d9-bf36-6394ef86c9d9.png'
favicon_path = 'favicon.png'

try:
    with Image.open(logo_path) as img:
        # Resize to 32x32 for favicon
        img.thumbnail((32, 32), Image.Resampling.LANCZOS)
        img.save(favicon_path, 'PNG')
        print(f"Created favicon at {favicon_path}")
except Exception as e:
    print(f"Failed to create favicon: {e}")
