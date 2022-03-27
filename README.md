# ECM3432-unit-tests

Unit-tests, regular-expressions, TDD

## The problem - validating user inputted data

User inputs generally need to be validated.  However, we can't always be sure that user inputted data has
been validated before being stored in a database or file.  A common example is email addresses.  These
are non-trivial strings that might be mistyped, or corrupted in any number of ways.

## Validating email addresses

One approach is to try and send an email to whatever address is given and only deem an address to be valid if a reply is received, or alternatively if no error is encountered when attempting to send.  This approach isn't always suitable,
for example when asking a user to enter an email address in a form.

Let's assume we want to establish whether some text is, or is not, acceptable as an email address. i.e. it has the correct format, even if no such email address exists.

Note. It is generally accepted that email addresses are case insensitive.  This is definitely true for domain names,
and should be true for the "local-part", i.e. the part of address before the '@' symbol.

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


## Resources

<https://datatracker.ietf.org/doc/html/rfc5322>