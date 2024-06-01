import requests

from number_facts import get_number_fact


class MockedResponse:

    def __init__(self, js_body) -> None:
        self.js_body = js_body

    def json(self):
        return self.js_body


def mock_get(*args, **kwargs):
    return MockedResponse(
        {
            "text": "3 is the cost in cents to make a $1 bill in the United States.",
            "found": "true",
        }
    )


def test_get_number_fact(monkeypatch):
    monkeypatch.setattr(requests, "get", mock_get)
    number = 3
    fact = "3 is the cost in cents to make a $1 bill in the United States."
    assert get_number_fact(number) == fact
