from application import db
from application.models import Songs

db.drop_all()
db.create_all()
test = Songs(song_name='Test',song_album='Test',song_artist='Test',song_key='Test',song_bpm=130)
test2 = Songs(song_name='Test2',song_album='Test2',song_artist='Test2',song_key='Test2',song_bpm=130)
db.session.add(test)
db.session.add(test2)
db.session.commit()