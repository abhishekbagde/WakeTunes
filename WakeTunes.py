import subprocess
import time
from urllib.parse import urlparse, parse_qs
import random

def search_random_song():
    # Logic to retrieve a random song URL
    # For now, return a hardcoded URL
    url_list = ["https://www.youtube.com/watch?v=4xDzrJKXOOY&ab_channel=LofiGirl",
                "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl",
                "https://www.youtube.com/watch?v=36YnV9STBqc&ab_channel=TheGoodLifeRadioxSensualMusique"]
    url = random.choice(url_list)
    return url

def open_url(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.netloc == "www.youtube.com" or parsed_url.netloc == "youtube.com":
            video_id = parse_qs(parsed_url.query).get("v", [None])[0]
            if video_id:
                youtube_url = f"https://www.youtube.com/watch?v={video_id}"
                subprocess.call(["open", youtube_url])
            else:
                print("Invalid YouTube URL.")
        else:
            print("The provided URL is not a YouTube URL.")
    except Exception as e:
        print(f"An error occurred: {e}")

def play_random_song():
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == 9 and current_time.tm_min == 0:
            random_song = search_random_song()
            open_url(random_song)
            # Delay for one day (24 hours * 60 minutes * 60 seconds)
            time.sleep(24 * 60 * 60)
        else:
            # Wait for 1 minute before checking the time again
            time.sleep(60)

# Start the program
try:
    play_random_song()
except KeyboardInterrupt:
    print("Program interrupted by user.")
