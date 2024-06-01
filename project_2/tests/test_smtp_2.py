def test_ehlo_function(smtp_connection) -> None:
    """
    Test the SMTP EHLO command

    Args:
        smtp_connection: A fixture to create an SMTP connection

    Returns:
        None
    """
    response, msg = smtp_connection.ehlo()
    print("Test EHLO 1 ")
    assert response == 250
    assert b"smtp.gmail.com" in msg


def test_noop_function(smtp_connection) -> None:
    """
    Test the SMTP NOOP command

    Args:
        smtp_connection: A fixture to create an SMTP connection

    Returns:
        None
    """
    response, msg = smtp_connection.noop()
    print("Test NOOP 1 ")
    assert response == 250
    assert b"OK" in msg


def test_ehlo_module(smtp_connection_module) -> None:
    """
    Test the SMTP EHLO command

    Args:
        smtp_connection: A fixture to create an SMTP connection

    Returns:
        None
    """
    response, msg = smtp_connection_module.ehlo()
    print("Test EHLO 2 ")
    assert response == 250
    assert b"smtp.gmail.com" in msg


def test_noop_module(smtp_connection_module) -> None:
    """
    Test the SMTP NOOP command

    Args:
        smtp_connection: A fixture to create an SMTP connection

    Returns:
        None
    """
    response, msg = smtp_connection_module.noop()
    print("Test NOOP 2 ")
    assert response == 250
    assert b"OK" in msg


def test_ehlo_session(smtp_connection_session) -> None:
    """
    Test the SMTP EHLO command

    Args:
        smtp_connection: A fixture to create an SMTP connection

    Returns:
        None
    """
    response, msg = smtp_connection_session.ehlo()
    print("Test EHLO 3 ")
    assert response == 250
    assert b"smtp.gmail.com" in msg


def test_noop_session(smtp_connection_session) -> None:
    """
    Test the SMTP NOOP command

    Args:
        smtp_connection: A fixture to create an SMTP connection

    Returns:
        None
    """
    response, msg = smtp_connection_session.noop()
    print("Test NOOP 3 ")
    assert response == 250
    assert b"OK" in msg
