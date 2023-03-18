import pytest
from app import home

@pytest.fixture()
def app():
    app = home("/")
    with app.app_context():
        "home.html"

    yield "home.html"

def app():
    app = about("/about")
    with app.app_context():
        "about.html"

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

    yield "about.html"

