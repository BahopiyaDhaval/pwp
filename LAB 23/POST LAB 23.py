#Write a code combining both validations into a single program.
#INPUT:
import re

# Function to validate PAN card number
def validate_pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    return bool(re.match(pattern, pan))

# Function to validate Email ID
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Input from user
pan_number = input("Enter PAN card number: ")
email_id = input("Enter email ID: ")

# Validation results
print("\nValidation Results:")
print(f"PAN card number: {'Valid' if validate_pan(pan_number) else 'Invalid'}")
print(f"Email ID: {'Valid' if validate_email(email_id) else 'Invalid'}")
