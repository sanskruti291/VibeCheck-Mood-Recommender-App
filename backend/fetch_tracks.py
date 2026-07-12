from dotenv import load_dotenv
load_dotenv()
import os
import pylast
print("API Key:", os.getenv("LASTFM_API_KEY"))
print("API Secret:", os.getenv("LASTFM_API_SECRET"))

def get_lastfm_client():
    return pylast.LastFMNetwork(
        api_key=os.environ["LASTFM_API_KEY"],
        api_secret=os.environ["LASTFM_API_SECRET"]
    )

client = get_lastfm_client()

def fetch_tracks(mood, limit=5):
    tag = client.get_tag(mood)
    top_tracks = tag.get_top_tracks(limit=limit)

    results = []

    for item in top_tracks:
        track = item.item

        try:
            cover_image = track.get_cover_image()
        except:
            cover_image = None

        results.append({
            "song": track.get_title(),
            "artist": track.get_artist().get_name(),
            "cover_image": cover_image,
            "url": track.get_url()
        })

    return results

if __name__ == "__main__":
    tracks = fetch_tracks("happy")

    for track in tracks:
        print(track)