import re
import logging

logging.basicConfig(level=logging.DEBUG)

def is_email_addr(text: str) -> bool:    
    match = re.match("^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", text, re.IGNORECASE)
    logging.debug(f"regex match is {match}")
    return match != None

if __name__ == "__main__":
    assert is_email_addr("m@saun.by"), "d m@saun.by is a valid email address"
    assert not is_email_addr("m at saun.by"), "d m@saun.by is not a valid email address"
