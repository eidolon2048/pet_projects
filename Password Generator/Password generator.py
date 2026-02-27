import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars
pwd_length = 20

while True:
    pwd = ''.join(secrets.choice(alphabet) for i in range(pwd_length))

    if (any(char in special_chars for char in pwd)and
        sum(char in digits for char in pwd)>=2):
            break
print("Your password is: \n")
print(pwd, "\n")