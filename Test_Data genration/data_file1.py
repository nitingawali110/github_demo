import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate fake data
def generate_fake_data(num_entries):
    fake_data = []
    for _ in range(num_entries):
        name = fake.name()
        phone_number = fake.phone_number()
        address = fake.address()
        fake_data.append({
            'Name': name,
            'Phone Number': phone_number,
            'Address': address
        })
    return fake_data

# Number of entries to generate
num_entries = 10

# Generate fake data
fake_data = generate_fake_data(num_entries)

# Convert fake data to a DataFrame
df = pd.DataFrame(fake_data)

# Save DataFrame to an Excel file
file_path = 'E:\\NitinPythonProject\\Test_Data genration\\testdata.xlsx'  # Corrected to .xlsx
df.to_excel(file_path, index=False)

print(f"Fake data saved to {file_path}")
