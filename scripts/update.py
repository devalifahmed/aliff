import os
import requests

API_URL = os.environ["API_URL"]
USER_AGENT = os.environ["API_USER_AGENT"]

headers = {
    "User-Agent": USER_AGENT,
    "Accept": "*/*"
}

response = requests.get(
    API_URL,
    headers=headers,
    timeout=30
)

response.raise_for_status()

print("HTTP status:", response.status_code)
print("Content type:", response.headers.get("Content-Type"))

content = response.text

if not content.lstrip().startswith("#EXTM3U"):
    raise RuntimeError("API did not return a valid M3U playlist")

print("Playlist received successfully")
