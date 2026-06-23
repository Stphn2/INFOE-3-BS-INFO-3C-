import random
import pandas as pd
from pprint import pprint
from faker import Faker

# Initialize the Faker generator
fake = Faker('en_US') 

def generate_raw_data(num_entries=25):
    raw_data = []
    for _ in range(num_entries):
        entry = {
            "name": fake.name(),
            "age": random.randint(18, 85),
            "zip_code": fake.postcode(),
            "salary": random.randint(35000, 150000),
            "medical_risk": random.choice(["Low", "Medium", "High"])
        }
        raw_data.append(entry)
    return raw_data

# Execute and print
data = generate_raw_data(25)
print("Generated 25 entries:")
pprint(data[:3])

# Save to the CSV file required for the next step
df = pd.DataFrame(data)
df.to_csv("employee_data.csv", index=False)
print("\nDataset saved to 'employee_data.csv'")