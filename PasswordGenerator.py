import secrets
import string

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


password_length = int(input("How many characters should this token be? (20 minimum is recommended) "))
password = generate_secure_password(password_length)
print(f"Generated Secure Password:\n {password}")
