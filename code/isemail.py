import re
import logging

logging.basicConfig(level=logging.DEBUG)


def is_email_addr(text: str) -> bool:
    """
    Use a regular expression to check if 'text' is a correctly formed
    email address.
    """
    regex = "^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$"
    match = re.match(regex, text, re.IGNORECASE)
    logging.debug(f"regex match is {match}")
    return match is not None


if __name__ == "__main__":
    assert is_email_addr("a@example.com"), "a valid email address"
    assert not is_email_addr("a at example.com"), "not a valid email address"
    assert not is_email_addr("")
    # assert not is_email_addr(None)
    # assert not is_email_addr(["hello"])
    # assert is_email_addr(b"m@example.com")
