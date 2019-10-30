import app
import pytest

@pytest.fixture
def api():
    return app.api

def test_response(api):
    hello = '{"name": "little orange"}'

    r = api.requests.get(url=api.url_for(app.route))
    assert r.text == hello
