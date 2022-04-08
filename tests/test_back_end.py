from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Songs

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY="testsecretkey",
            WTF_CSRF_ENABLED=False
            )
        return app
    
    def setUp(self):
        db.create_all()
        test = Songs(song_name='Test',song_album='Test',song_artist='Test',song_key='Test',song_bpm=130)
        db.session.add(test)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):
    def test_home_get(self):
        reponse = self.client.get(url_for('home'))
        self.assertEqual(response.staus_code, 200)