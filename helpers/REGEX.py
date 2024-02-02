import re

USERNAME = re.compile(r"^[\w \[\]-]{2,20}$")
EMAIL = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
