import unittest
from unittest.mock import MagicMock
from flask import Flask, render_template, request
from variable import cursor
from app import top20

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n', response.data)

    def test_invalid_url(self):
        response = self.client.get('/invalid')
        self.assertEqual(response.status_code, 404)


    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n', response.data)

    def test_contactus_page(self):
        response = self.client.get('/contactus')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n', response.data)

    def test_home_page(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n', response.data)

    def test_top20_page(self):
        # mock the cursor object and its execute and fetchall methods
        cursor.execute = MagicMock(return_value=None)
        cursor.fetchall = MagicMock(return_value=[(1, 1, 'trigger', 'description', '2023-03-14 10:00:00')])

        # call the top20 route and check the response
        with self.app.test_request_context('/top20'):
            response = top20()
            self.assertIn(b'Top 20', response.data)
            self.assertIn(b'1', response.data)
            self.assertIn(b'trigger', response.data)
            self.assertIn(b'description', response.data)
            self.assertIn(b'2023-03-14 10:00:00', response.data)


if __name__ == '__main__':
    unittest.main()
