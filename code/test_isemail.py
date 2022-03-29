# Run these tests using Pytest
# python -m pytest .

from isemail import is_email_addr


def test_good_email():
    test_addr = "bob@example.com"
    result = is_email_addr(test_addr)
    assert result is True


def test_bad_email():
    test_addr = "bob at example.com"
    result = is_email_addr(test_addr)
    assert result is False

