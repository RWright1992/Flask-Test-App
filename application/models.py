#importing database instance
from application import db


#creating song schema with name, album, artist, 
class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(100), nullable=False)
    song_album = db.Column(db.String(100), nullable=False)
    song_artist = db.Column(db.String(100), nullable=False)
    song_key = db.Column(db.String(10), nullable=False)
    song_bpm = db.Column(db.Integer, nullable=False)