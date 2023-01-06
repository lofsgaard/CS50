import validators

email = input("What's your email address?: ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")