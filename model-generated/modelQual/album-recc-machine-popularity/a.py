def recommend_albums(albums, genre):
    # Filter albums by genre
    filtered_albums = [album for album in albums.values() if genre in album['genres']]
    
    # Sort albums by popularity
    sorted_albums = sorted(filtered_albums, key=lambda x: x['streams'], reverse=True)
    
    return sorted_albums

# Mock albums
albums = {
    'You Won\'t Go Before You\'re Supposed To': {
        'name': 'You Won\'t Go Before You\'re Supposed To',
        'artist': 'Knocked Loose',
        'genres': ['Metalcore'],
        'streams': 59116213
    },
    'CONCRETE JUNGLE [The OST]': {
        'name': 'CONCRETE JUNGLE [The OST]',
        'artist': 'Bad Omens',
        'genres': ['Industrial', 'Experimental', 'Lo-fi'],
        'streams': 215235222
    },
    'Graduation': {
        'name': 'Graduation',
        'artist': 'Kanye West',
        'genres': ['Pop Rap', 'Hip Hop'],
        'streams': 1759116213
    },
    'Illmatic': {
        'name': 'Illmatic',
        'artist': 'Nas',
        'genres': ['Hip Hop', 'Jazz Rap'],
        'streams': 215235222
    },
    'Hybrid Theory': {
        'name': 'Hybrid Theory',
        'artist': 'Linkin Park',
        'genres': ['Rap Rock', 'Nu Metal'],
        'streams': 78526992
    }
}

# Search for Metalcore albums
recommended_albums = recommend_albums(albums, 'Metalcore')

for album in recommended_albums:
    print(f"{album['name']} by {album['artist']}")