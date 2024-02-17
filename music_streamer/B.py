import datetime
import json

class Song:
    def __init__(self, song_id, artist, duration, release_year):
        self.song_id = song_id
        self.artist = artist
        self.duration = datetime.timedelta(seconds=duration)
        self.release_year = release_year

    def __repr__(self):
        return f"Song({self.song_id}, {self.artist}, {self.duration}, {self.release_year})"

    def rate(self, rating):
        self.rating = rating

    def add_to_playlist(self, playlist):
        playlist.append(self)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def __repr__(self):
        return f"Playlist({self.name}, {len(self.songs)} songs)"

    def add_song(self, song):
        song.add_to_playlist(self)

    def calculate_total_duration(self):
        total_duration = datetime.timedelta()
        for song in self.songs:
            total_duration += song.duration
        return total_duration

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
        data.append({**song.__dict__, 'rating': song.rating})
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    # Load songs from file
    songs = load_songs_from_file('/root/code-sandbox/randomJS/matrix_manipulation_scripts/music_streamer/songs.json')

    # Create a playlist
    playlist = Playlist('Favorites')

    # Add songs to playlist and rate them
    playlist.add_song(songs[0])
    playlist.add_song(songs[1])
    playlist.add_song(songs[2])
    songs[0].rate(4)
    songs[1].rate(3)
    songs[2].rate(5)

    # Calculate total duration of playlist
    total_duration = playlist.calculate_total_duration()
    print(f"Total duration: {total_duration}")

    # Save playlist to file
    save_playlist_to_file(playlist, 'favorites.json')

if __name__ == '__main__':
    main()