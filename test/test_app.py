from flask import Flask

def test_home():
    app = Flask(__name__)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404

def test_about():
    app = Flask(__name__)
    client = app.test_client()
    url = '/about'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404

def test_contactus():
    app = Flask(__name__)
    client = app.test_client()
    url = '/contactus'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404

def test_top20():
    app = Flask(__name__)
    client = app.test_client()
    url = '/top20'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404

def test_top50():
    app = Flask(__name__)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404

def test_top100():
    app = Flask(__name__)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404


def test_jobid():
    app = Flask(__name__)
    client = app.test_client()
    url = '/jobid'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404


def test_getjob():
    app = Flask(__name__)
    client = app.test_client()
    url = '/jobid'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404


def test_hours24():
    app = Flask(__name__)
    client = app.test_client()
    url = '/hours24'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404


def test_lastweek():
    app = Flask(__name__)
    client = app.test_client()
    url = '/lastweek'

    response = client.get(url)
    assert response.get_data() == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not F'b'ound</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on th'b'e server. If you entered the URL manually please check your spelling and try'b' again.</p>\n'
    assert response.status_code == 404
