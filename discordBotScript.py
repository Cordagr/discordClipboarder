import os
import time 
import re
import pyperclip
import requests
from urllib.parse import urlparse

# Folder to save images
SAVE_DIR = "discord_image_downloads"
os.makedirs(SAVE_DIR, exist_ok=True)

# Regular expression to detect URLS (Formatted as JPG,GIF,PNG, ...)
IMAGE_URL_PATTERN = re.compile(r'https?://\S+\.(?:png|jpg|jpeg|gif|webp)')

# Detects if cipboard content is a valid image using REGEX listed above 
def is_valid_image_url(url):
  return bool(IMAGE_URL_PATTERN.match(url))

def download_image(url):
  try:
    response = requests.get(url, stream = True)
    response.raise_for_status()

parsed_url = urlparse(url)
fileame = os.path.basename(parsed_url.path)
if not filename:
  filename = f"image{int(time.time())}".png

save_path = os.path.join(SAVE_DIR, filename)

# Save image
with open(save_path, "wb") as img_file:
  for chunk in response.iter_content(1024):
    img.file.write(chunk)
  print("Image Saved: {saved_path}")

except requests.exceptions.RequestException as e:
  print("Failed to download image: {e}")





