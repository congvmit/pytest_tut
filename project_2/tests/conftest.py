import smtplib

import pytest


@pytest.fixture(scope="function", autouse=True)
def smtp_connection() -> smtplib.SMTP:
    print("Setup Function")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("Teardown Function")


@pytest.fixture(scope="module", autouse=True)
def smtp_connection_module() -> smtplib.SMTP:
    print("Setup Module")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("Teardown Module")


@pytest.fixture(scope="session", autouse=True)
def smtp_connection_session() -> smtplib.SMTP:
    print("Setup Session")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("Teardown Session")


@pytest.fixture(scope="class", autouse=True)
def smtp_connection_class() -> smtplib.SMTP:
    print("Setup Class")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("Teardown Class")
