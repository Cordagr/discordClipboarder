import os
import time 
import re
import pyperclip
import requests
from urllib.parse import urlparse
import threading
import discord
import tkinkter import scrolledText
from discord.ext import commands
from urllib.parse import urlparse

# Configurations
DISCORD_BOT_TOKEN = "YOUR_BOT_TOKEN" # Replace with your bot token
DISCORD_GUILD_ID = YOUR_GUILD_ID # Replace with discord server ID
# Folder to save images
SAVE_DIR = "discord_image_downloads"
os.makedirs(SAVE_DIR, exist_ok=True)

# Setup bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!",intent=intents)
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

# Uploads image to private discord
async def upload_image_to_discord(file_path):
  guild = bot.get_guild(DISCORD_GUILD_ID)
  if guild is None:
    print(" Bot is not connected to the server")
    return
  with open(file_path,"rb") as file:
    image_bytes = file.read()
  # Uploading image as emoji
emoji_name = os.path.splitext(os.path.basename(file_path))[0]
try:
  emoji = await guild.create_custom_emoji(name=emoji_name, image=image_bytes)
  print("Emoji successfuly uploaded::{emoji.name}:")
except discord.HTTPException as e:
  printf("Failed to upload emoji: {e}")

# Monitoring clipboard for image URLS
def monitor_clipboard():
  last_clipboard_content = ""
  print("Clipboard Monitoring is active")

  while True:
    time.sleep(1)
    clipboard_content = pyperclip.pase.strip()
    if clipboard_content != last_clipboard_content:
      last_clipboard_content = clipboard_content 
      if is_image_url(clipboard_content):
        print("New Image URL detected:{clipboard_content}")
        file_path = download_image(clipboard_content)
        if file_path:
          bot.loop.create(upload_image_to_discord(file_path))

 async def on_read():
   printf("Logged in as user: {bot.user}")

 if name = "__main__":
   import threading
   # Seperate Threat to run monitorting discord 
   clipboard_thread = threading_Thread(target = monitor_clipboard, daemon = True)
   clipboard_thread.start()

   # Running discord bot
   bot.run(DISCORD_BOT_TOKEN)

   



