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

    yield "about.html"

