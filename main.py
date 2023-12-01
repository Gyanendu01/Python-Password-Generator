import getpass
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_valid_password(password):
    # Check if the password meets the specified criteria
    return (
        len(password) >= 8
        and any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in string.punctuation for c in password)
    )

def main():
    password_length = int(input("\tEnter the desired password length: "))
    num_passwords = int(input("\tEnter the number of passwords to generate: "))

    for _ in range(num_passwords):
        generated_password = generate_password(password_length)

        # Ensure the generated password meets the criteria
        while not is_valid_password(generated_password):
            generated_password = generate_password(password_length)

        print("\n\tGenerated Password: {}".format(generated_password))

if __name__ == "__main__":
    main()
