import re
import json


import re
import json

def validate_user(username, email, password):

    username_pattern = re.compile(r'^[A-Za-z ]{6,15}$')
    email_pattern = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
    password_pattern = re.compile(
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    )

    result = {}

    # Username validation
    if username_pattern.fullmatch(username):
        result["username"] = "valid"
    else:
        result["username"] = "invalid"

    # Email validation
    if email_pattern.fullmatch(email):
        result["email"] = "valid"
    else:
        result["email"] = "invalid"

    # Password validation
    if password_pattern.fullmatch(password):
        result["password"] = "valid"
    else:
        result["password"] = "invalid"

    return result


# Input
username = input("Enter username: ")
email = input("Enter email: ")
password = input("Enter password: ")

details = validate_user(username, email, password)

# Pretty output
print(json.dumps(details, indent=4))
