import random

def generate_mobile_number():
    # Generate the first digit (shouldn't be 0)
    first_digit = random.choice([7, 8, 9])
    # Generate the remaining 9 digits
    remaining_digits = random.randint(100000000, 999999999)
    # Combine the first digit with the remaining digits
    mobile_number = f"{first_digit}{remaining_digits}"
    return mobile_number

# Generate a random 10-digit mobile number
print(generate_mobile_number())
