class Track:
    def __init__(self, id, tempo, key, length, number_series):
        self.id = id
        self.tempo = tempo
        self.key = key
        self.length = length
        self.number_series = number_series

    def decrypt_position(self):
        # Decrypt the position of the track based on the number series
        # This is just a placeholder, the actual decryption algorithm is not provided
        return sum(self.number_series) % len(tracks)

tracks = [
    Track(1, 120, 'C', 4, [1, 2, 3, 4]),
    Track(2, 110, 'G', 3, [5, 6, 7]),
    Track(3, 130, 'F', 5, [8, 9, 10, 11, 12]),
    Track(4, 100, 'E', 2, [13, 14]),
    Track(5, 90, 'D', 6, [15, 16, 17, 18, 19, 20])
]

# Shuffle the tracks
import random
random.shuffle(tracks)

# Reorder the tracks based on their decrypted positions
tracks.sort(key=lambda track: track.decrypt_position())

# Print the reordered tracks
for track in tracks:
    print(f'Track ID: {track.id}, Tempo: {track.tempo}, Key: {track.key}, Length: {track.length}, Number Series: {track.number_series}')

