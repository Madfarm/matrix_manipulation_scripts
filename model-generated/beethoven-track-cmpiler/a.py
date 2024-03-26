import random

# Define a Track class
class Track:
    def __init__(self, id, tempo, key, length, encrypted_position, reversed=False):
        self.id = id
        self.tempo = tempo
        self.key = key
        self.length = length
        self.encrypted_position = encrypted_position
        self.reversed = reversed

    def decrypt_position(self):
        # For simplicity, let's assume the decryption is just summing the encrypted numbers
        return sum(self.encrypted_position)

# Create a list of tracks
tracks = [
    Track(1, 120, 'C', 300, [1, 2, 3]),
    Track(2, 120, 'C', 250, [4, 5, 6]),
    Track(3, 120, 'C', 200, [7, 8, 9]),
    Track(4, 120, 'C', 220, [10, 11, 12]),
    Track(5, 120, 'C', 280, [13, 14, 15]),
]

# Shuffle the tracks
random.shuffle(tracks)

# Try to reconstruct the symphony
reconstructed_symphony = []
for track in tracks:
    # If the track has been played in reverse, reverse the decrypted position
    position = track.decrypt_position() if not track.reversed else -track.decrypt_position()
    reconstructed_symphony.append((position, track))

# Sort the symphony by the decrypted positions
reconstructed_symphony.sort()

# Print the reconstructed symphony
for position, track in reconstructed_symphony:
    print(f'Track {track.id} (Tempo: {track.tempo}, Key: {track.key}, Length: {track.length}s) should be played at position {position}.')