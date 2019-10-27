import hej
import pytest

@pytest.fixture
def api():
    return hej.api

def test_response(api):
    hello = '{"name": "little orange"}'

    r = api.requests.get(url=api.url_for(hej.route))
    assert r.text == hello
