# conftest.py

import pytest
import requests

# @pytest.fixture(autouse=True)
# def disable_network_calls(monkeypatch):
#     def stunted_get(*args, **kwargs):
#         raise RuntimeError("Network access not allowed during testing!")

#     monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())


# disable_network_calls(pytest.MonkeyPatch())
