import json

class Song:
    def __init__(self, song_id, artist, duration, release_year):
        self.song_id = song_id
        self.artist = artist
        self.duration = duration
        self.release_year = release_year
        self.rating = None

    def __repr__(self):
        return f"Song({self.song_id}, {self.artist}, {self.duration}, {self.release_year})"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __repr__(self):
        return f"Playlist({self.name}, {len(self.songs)} songs)"

def load_songs_from_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        songs = []
        for song_data in data:
            song = Song(**song_data)
            songs.append(song)
        return songs

def save_playlist_to_file(playlist, filename):
    data = []
    for song in playlist.songs:
        song_data = song.__dict__.copy()
        song_data['rating'] = song.rating
        data.append(song_data)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_rating(song):
    print(f"{song.song_id}: {song.artist} - Rate this song:")
    rating = input("1-5 (1=bad, 5=awesome): ")
    while rating not in ["1", "2", "3", "4", "5"]:
        print("Invalid rating. Try again!")
        rating = input("1-5 (1=bad, 5=awesome): ")
    song.rating = int(rating)

def main():
    # Load songs from file
    songs = load_songs_from_file('/root/code-sandbox/randomJS/matrix_manipulation_scripts/music_streamer/songs.json')

    # Create a playlist
    playlist = Playlist('Favorites')

    # Add all songs to playlist
    for song in songs:
        playlist.add_song(song)
        get_rating(song)

    # Save playlist to file
    save_playlist_to_file(playlist, 'favorites.json')

if __name__ == '__main__':
    main()