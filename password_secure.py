import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    special_char_error = not re.search(r"\W", password)

    errors = []
    if length_error:
        errors.append("Password should be at least 8 characters long.")
    if digit_error:
        errors.append("Password should contain at least one digit.")
    if uppercase_error:
        errors.append("Password should contain at least one uppercase letter.")
    if lowercase_error:
        errors.append("Password should contain at least one lowercase letter.")
    if special_char_error:
        errors.append("Password should contain at least one special character.")

    if not errors:
        return "Password is strong and meets the complexity requirements."
    else:
        return "Password is weak. Please consider the following:\n" + "\n".join(errors)

# Example usage
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
