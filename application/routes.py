# import render_template function from the flask module
from flask import render_template, url_for, redirect, request
# import the app object from the ./application/__init__.py
from application import app, db
# importing Songs and SetList Class from models.py
from application.models import Songs
# importing song form from forms.py
from application.forms import SongForm

@app.route('/')
@app.route('/home')
def home():
	return render_template('layout.html', title='Home')

@app.route('/songs')
def songs():
    songdata = Songs.query.all()
    return render_template('songs.html', title='Songs', songs=songdata)

@app.route('/addsong', methods=['GET', 'POST'])
def addsong():
    form = SongForm()
    if form.validate_on_submit():
        songData = Songs(
			song_name = form.song_name.data,
			song_album = form.song_album.data,
			song_artist = form.song_artist.data,
			song_key = form.song_key.data,
			song_bpm = form.song_bpm.data
		)
        db.session.add(songData)
        db.session.commit()
        return redirect(url_for('songs'))
    else:
        print(form.errors)
    return render_template('addsong.html', title='Add Song', form=form)


@app.route('/songs/delete/<id>', methods=['GET', 'POST'])
def song_delete(id):
    songdel = Songs.query.filter_by(id=id).first()
    db.session.delete(songdel)
    db.session.commit()
    return redirect(url_for('songs'))

@app.route('/songs/edit/<id>', methods=['GET', 'POST'])
def song_edit(id):
    song = Songs.query.filter_by(id=id).first()
    form = SongForm()
    if form.validate_on_submit():
        song.song_name = form.song_name.data
        song.song_album = form.song_album.data
        song.song_artist = form.song_artist.data
        song.song_key = form.song_key.data
        song.song_bpm = form.song_bpm.data
        db.session.commit()
        return redirect(url_for('songs'))
    elif request.method == 'GET':
        form.song_name.data = song.song_name
        form.song_album.data = song.song_album
        form.song_artist.data = song.song_artist
        form.song_key.data = song.song_key
        form.song_bpm.data = song.song_bpm
    return render_template('editsong.html', title='Edit Song', form=form)