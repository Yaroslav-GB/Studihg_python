import json

favourite_tracks = [
    {'name': 'Pit of Fire', 'artist': '3TEETH'},
    {'name': 'Snuff', 'artist': 'Slipknot'},
    {'name': 'New Faith', 'artist': 'Slayer'},
]

with open('track.json', 'w', encoding='utf-8') as fp:
    json.dump(favourite_tracks, fp)

print("Ready")
