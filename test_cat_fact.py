from cat_fact import get_cat_fact

# def test_cat_fact_no_monkeypatch():
#     code, response = get_cat_fact()
#     assert code == 200


def test_cat_fact_w_monkeypatch(monkeypatch):
    class MockResponse:

        def __init__(self) -> None:
            self.status_code = 200
            self.url = "https://meowfacts.herokuapp.com/"

        def json(self):
            return {
                "data": ["Mother cats teach their " 
                         "kittens to use the litter box."]
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    assert get_cat_fact() == (
        200,
        {"data": ["Mother cats " 
                  "teach their kittens " 
                  "to use the litter box."]},
    )
