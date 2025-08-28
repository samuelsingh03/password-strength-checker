import re
import hashlib
from zxcvbn import zxcvbn

def check_password_strength(password):
    result = zxcvbn(password)
    score = result['score']  # 0 = weak, 4 = very strong
    feedback = result['feedback']

    print(f"Password: {password}")
    print(f"Strength Score: {score}/4")
    print(f"Feedback: {feedback}")

    # Hash the password (simulation of storage)
    hashed = hashlib.sha256(password.encode()).hexdigest()
    print(f"SHA-256 Hash: {hashed}\n")

if __name__ == "__main__":
    while True:
        pwd = input("Enter a password (or type 'exit' to quit): ")
        if pwd.lower() == 'exit':
            break
        check_password_strength(pwd)
