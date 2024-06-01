class TestSMTP1:

    def test_ehlo(self, smtp_connection_class) -> None:
        """
        Test the SMTP EHLO command in a class

        Args:
            smtp_connection: A fixture to create an SMTP connection

        Returns:
            None
        """
        response, msg = smtp_connection_class.ehlo()
        print("Test EHLO 1 in Class...")
        assert response == 250
        assert b"smtp.gmail.com" in msg

    def test_noop(self, smtp_connection_class) -> None:
        """
        Test the SMTP NOOP command in a class

        Args:
            smtp_connection: A fixture to create an SMTP connection

        Returns:
            None
        """
        response, msg = smtp_connection_class.noop()
        print("Test NOOP 1 in Class...")
        assert response == 250
        assert b"OK" in msg
