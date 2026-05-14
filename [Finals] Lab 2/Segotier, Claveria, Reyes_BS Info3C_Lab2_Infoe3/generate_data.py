from faker import Faker
import random
import pandas as pd
from pprint import pprint

# Initialize the Faker generator
fake = Faker('en_US')  

def generate_raw_data(num_entries=25):  # Default is now 25
    raw_data = []
    
    for _ in range(num_entries):
        entry = {
            "name": fake.name(),
            "age": random.randint(18, 85),
            "zip_code": fake.postcode(),
            "salary": random.randint(35000, 160000),
            "medical_risk": random.choice(["Low", "Medium", "High"])
        }
        raw_data.append(entry)
        
    return raw_data

# Generate 25 entries (or change to any number >= 25)
raw_data = generate_raw_data(25)  # Change 25 to desired number

# Display the result
print(f"Generated {len(raw_data)} entries:\n")
pprint(raw_data[:3])  # Show first 3 records only

# Convert to DataFrame and save to CSV
df = pd.DataFrame(raw_data)
df.to_csv('employee_data.csv', index=False, encoding='utf-8-sig')

print("\n✅ Dataset saved to 'employee_data.csv'")
print(f"Total records: {len(raw_data)}")