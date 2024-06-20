import tkinter as tk
import webbrowser
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import random
from config import API_KEY  # Import API key from config.py

class YouTubeShortsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Shorts Viewer")
        self.root.geometry("800x600")

        self.shorts_urls = []
        self.current_short_index = 0

        self.web_frame = tk.Frame(self.root)
        self.web_frame.pack(fill=tk.BOTH, expand=True)

        self.open_short_button = tk.Button(self.web_frame, text="Open Short", command=self.open_current_short)
        self.open_short_button.pack(pady=10)

        self.scroll_next_button = tk.Button(self.web_frame, text="Next Short", command=self.scroll_to_next_short)
        self.scroll_next_button.pack(pady=10)

        # Fetch initial set of Shorts URLs
        self.fetch_shorts_urls()

    def fetch_shorts_urls(self):
        try:
            youtube = build('youtube', 'v3', developerKey=API_KEY)

            # Example: Search for YouTube Shorts videos
            request = youtube.search().list(
                part='snippet',
                q='#shorts',  # Search query for Shorts
                type='video',
                videoDuration='short',
                maxResults=50  # Adjust as needed
            )

            response = request.execute()

            # Extract video IDs from search results
            self.shorts_urls = ['https://www.youtube.com/watch?v=' + item['id']['videoId'] for item in response['items']]

        except HttpError as e:
            print(f"An error occurred: {e}")

    def open_current_short(self):
        if self.shorts_urls:
            url = self.shorts_urls[self.current_short_index]
            webbrowser.open_new(url)

    def scroll_to_next_short(self):
        if self.shorts_urls:
            self.current_short_index = (self.current_short_index + 1) % len(self.shorts_urls)
            self.open_current_short()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeShortsApp(root)
    root.mainloop()
