import unittest

from party import app
from model import db, example_data, connect_to_db


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn(b"board games, rainbows, and ice cream sundaes", result.data)

    def test_no_rsvp_yet(self):
        result = self.client.post("/rsvp",
                              data={"name": "Jane",
                                    "email": "jane@jane.com"},
                              follow_redirects=True)

        print("FIXME")

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={"name": "Jane",
                                        "email": "jane@jane.com"},
                                  follow_redirects=True)
        # FIXME: Once we RSVP, we should see the party details, but
        # not the RSVP form
        print("FIXME")


class PartyTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        self.client = app.test_client()
        app.config['TESTING'] = True
        connect_to_db(app, "postgresql:///testdb")
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        # (uncomment when testing database)
        db.session.close()
        db.drop_all()

    def test_games(self):
        # FIXME: test that the games page displays the game from example_data()
        print("FIXME")
        result = self.client.get("/games")
        self.assertIn(b"Power Grid", result.data)

if __name__ == "__main__":
    unittest.main()
