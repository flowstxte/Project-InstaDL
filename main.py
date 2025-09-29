import instaloader
import re
import hashlib
import os

reel_links = [
    # Add your Instagram reel URLs here
    # "https://www.instagram.com/reel/1234567890",
    # "https://www.instagram.com/reel/abcdefghij"
]

def get_shortcode_from_url(url):
    match = re.search(r"instagram\.com/reel/([A-Za-z0-9_\-]+)/?", url)
    if match:
        return match.group(1)
    return None

def generate_link_hash(url):
    return hashlib.sha256(url.encode('utf-8')).hexdigest()

def download_reels(urls):
    loader = instaloader.Instaloader()

    # Uncomment the following lines and fill in your details if you need to log in
    # try:
    #     loader.load_session_from_file("your_username")
    # except FileNotFoundError:
    #     username = "your_username"
    #     password = "your_password"
    #     loader.login(username, password)
    #     print(f"Logged in as {username}")

    for url in urls:
        shortcode = get_shortcode_from_url(url)
        if not shortcode:
            print(f"Invalid URL: {url}")
            continue

        folder_name = shortcode 
        
        try:
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            
            loader.download_post(post, target=folder_name)
            print(f"Downloaded: {url} into folder: {folder_name}")
        except Exception as e:
            print(f"Failed to download {url}\n   Reason: {e}")

download_reels(reel_links)
