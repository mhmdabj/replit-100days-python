def get_spotify_tracks_stub(year):
    # This is a stub for the Spotify API lesson.
    return [f"Track {i} from {year}" for i in range(1, 11)]

if __name__ == "__main__":
    print(get_spotify_tracks_stub(1990)) 