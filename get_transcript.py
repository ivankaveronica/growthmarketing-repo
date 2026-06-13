import os
import sys
import requests
from datetime import date
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SUPADATA_API_KEY")
BASE_URL = "https://api.supadata.ai/v1/youtube/transcript"


def extract_video_id(url):
    parsed = urlparse(url)
    if parsed.hostname in ("youtu.be",):
        return parsed.path.lstrip("/")
    qs = parse_qs(parsed.query)
    ids = qs.get("v")
    if ids:
        return ids[0]
    raise ValueError(f"Could not extract video ID from URL: {url}")


def fetch_transcript(video_url):
    response = requests.get(
        BASE_URL,
        params={"url": video_url},
        headers={"x-api-key": API_KEY},
    )
    response.raise_for_status()
    data = response.json()

    # Supadata returns a list of segments with 'text' fields
    segments = data.get("content", [])
    if isinstance(segments, list):
        return " ".join(seg.get("text", "") for seg in segments)
    # Fallback if the API returns a plain string
    return str(segments)


def save_transcript(expert_name, video_url, transcript):
    video_id = extract_video_id(video_url)
    folder = os.path.join("research", "youtube-transcripts", expert_name)
    os.makedirs(folder, exist_ok=True)

    filename = f"{expert_name}-{video_id}.txt"
    filepath = os.path.join(folder, filename)

    header = (
        f"Expert: {expert_name}\n"
        f"Video URL: {video_url}\n"
        f"Date collected: {date.today().isoformat()}\n"
        f"{'=' * 60}\n\n"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + transcript)

    return filepath


def main():
    if len(sys.argv) != 3:
        print("Usage: python get_transcript.py <youtube-url> <expert-name>")
        sys.exit(1)

    video_url = sys.argv[1]
    expert_name = sys.argv[2]

    if not API_KEY:
        print("Error: SUPADATA_API_KEY not set in .env")
        sys.exit(1)

    print(f"Fetching transcript for: {video_url}")
    transcript = fetch_transcript(video_url)

    filepath = save_transcript(expert_name, video_url, transcript)
    print(f"Saved to: {filepath}")


if __name__ == "__main__":
    main()
