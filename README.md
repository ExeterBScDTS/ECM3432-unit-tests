# ECM3432-unit-tests

Unit-tests, regular-expressions, TDD

## The problem - validating user inputted data

User inputs generally need to be validated.  However, we can't always be sure that user inputted data has
been validated before being stored in a database or file.  A common example is email addresses.  These
are non-trivial strings that might be mistyped, or corrupted in any number of ways.

## Validating email addresses

One approach to validating email addresses is to try and send an email to whatever address is given and only deem an address to be valid if a reply is received, or alternatively if no error is encountered when attempting to send.  This approach isn't always suitable,
for example when asking a user to enter an email address in a form.

Let's assume, before trying to send a message, we first want to establish whether some text is, or is not, acceptable as an email address. i.e. it has the correct format, even if no such email address exists.


What we require, in whatever programming language we are using, is a function that will return a boolean value
indicating if a given text string is, or is not an email address.

e.g.

```python
def is_email_addr(text: str) -> bool:
    is_valid: bool = False
    ...
    return is_valid
```

## Regular expressions

A Regular Expression (regex) is a character pattern used to search text for matches.  A regular
expression can be as simple as a single character or word, in which case it would match any
occurrences or that text or word in a string.  More often regular expressions use characters
that have special meanings.  For example, ```[a-z]``` would match any single letter in the range a to z.  If followed by ```+``` one or more occurrences of the preceding pattern, e.g. ```(spam)+``` would match "spam", "spamspam", etc.

Most widely used programming languages have a regex library, and are ideally suited to problem such as
checking if a string is, or contains, an email address.

The following regex will match correctly formed email addresses.

```python
"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$"
```

Source: <https://www.regular-expressions.info/email.html>

However, it's not easy to see how this works, so we really should test it to be sure it does what we want it to do.

Note. It is generally accepted that email addresses are case insensitive.  This is definitely true for domain names,
and should be true for the "local-part", i.e. the part of address before the '@' symbol.

## Unit-tests

Unit-tests are small, simple, tests, that are easily automated.  They have the following structure -

* initialization
* call the object to be tested
* assert some condition

These tests can be used to establish that objects (typically functions) do what is expected, and also that they can handle abnormal inputs appropriately - they don't cause your program to crash.

## Pytest

Pytest is an easy to use testing framework for Python that can find and run unit-tests, and generate a test report.

Tests of our email validator might look like this -

```Python
from emailcheck import is_email_addr


def test_good_email():
    test_addr = "bob@example.com"
    result = is_email_addr(test_addr)
    assert result == True


def test_bad_email():
    test_addr = "bob at example.com"
    result = is_email_addr(test_addr)
    assert result == False

```

These tests are run using the Pytest framework, e.g.

```sh
cd code
python3 -m pytest .
```

## Testing goals

Validation testing - Does the system operate as intended?

Defect testing - Are there faults in the software where it fails to meet its specification?

![testing-input-output-model.png](testing-input-output-model.png)

Can our function distinguish good email addresses from bad/not email addresses?

Can our function handle bad or missing data?

## Selecting tests

There are almost infinite valid email addresses, and similarly for invalid addresses.  What is needed is selection of useful input test candidates.

![equivalence-partitioning.png](equivalence-partitioning.png)

## Exercise -

Propose suitable test inputs for the ```is_email_addr()``` function, by identifying suitable
equivalence partitions.

## Resources

<https://datatracker.ietf.org/doc/html/rfc5322>