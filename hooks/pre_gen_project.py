import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"


module_name = "{{cookiecutter.module_name}}"
author_email = "{{cookiecutter.author_email}}"


if not re.match(MODULE_REGEX, module_name):
    print(f"ERROR: The python module name is not valid: {module_name}")
    sys.exit(1)

if not re.match(EMAIL_REGEX, author_email):
    print(f"ERROR: Author email is invalid: {author_email}")
    sys.exit(1)
