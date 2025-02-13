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
