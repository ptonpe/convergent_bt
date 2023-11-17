from dotenv import load_dotenv
import os


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Spotify API credentials
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'your_redirect_uri'

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='user-library-read'))

# Searching Song in API
song_name = "22"
artist_name = "Taylor Swift"
results = sp.search(q=f"track:{song_name} artist:{artist_name}", type='track', limit=1)

# Retrieving song ID from API
if results['tracks']['items']:
    target_track_id = results['tracks']['items'][0]['id']

    # Audio features/key metrics of song
    target_audio_features = sp.audio_features([target_track_id])[0]

    # Step 3: Cosine similarity, not sure on how this works/how accurate it is
    def cosine_similarity_metric(target_features, other_features):
        target_vector = np.array([target_features['danceability'], target_features['energy']])
        other_vector = np.array([other_features['danceability'], other_features['energy']])
        similarity = cosine_similarity([target_vector, other_vector])
        return similarity[0, 1]

    #Searching for similar songs based on metric
    user_top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')
    similar_songs = []

    for track in user_top_tracks['items']:
        track_id = track['id']
        if track_id != target_track_id:
            other_audio_features = sp.audio_features([track_id])[0]
            similarity_score = cosine_similarity_metric(target_audio_features, other_audio_features)
            similar_songs.append({'id': track_id, 'name': track['name'], 'artist': track['artists'][0]['name'], 'similarity': similarity_score})

    # Sort the list of similar songs by similarity score
    similar_songs.sort(key=lambda x: x['similarity'], reverse=True)

    #Filter recommendations by language
    track_languages = {
        'SPOTIFY_TRACK_ID_1': 'English',
        'SPOTIFY_TRACK_ID_2': 'Spanish',
        'SPOTIFY_TRACK_ID_3': 'English',
        # Add more tracks and languages
    }

    # Filter recommendations by the desired language
    desired_language = 'Spanish'
    language_filtered_recommendations = [
        {'name': song['name'], 'artist': song['artist']} for song in similar_songs
        if track_languages.get(song['id'], '') == desired_language
    ]

    # Print the recommended songs in new language to the terminal
    for recommendation in language_filtered_recommendations:
        print(f"Recommended Song: {recommendation['name']} by {recommendation['artist']}")

else:
    print(f"No results found for the song {song_name} by {artist_name}")
