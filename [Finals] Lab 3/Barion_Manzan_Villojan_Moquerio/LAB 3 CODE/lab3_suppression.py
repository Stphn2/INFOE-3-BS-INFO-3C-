import random
import csv
import copy
from faker import Faker

random.seed(42)
Faker.seed(42)

# Generate raw_data
fake = Faker()
raw_data = []

for _ in range(30):
    raw_data.append({
        "name": fake.name(),             
        "age": random.randint(18, 70),   
        "zip_code": fake.zipcode(),     
        "salary": random.randint(30000, 150000),
        "medical_risk": random.choice(["Low", "Medium", "High"])
    })

# --- TASK 1: Load the Data ---
new_data = copy.deepcopy(raw_data) 

# --- TASK 2: Define the "Hit List" ---
hit_list = ["name", "medical_risk"] 

# --- TASK 3: Execute Suppression ---
for record in new_data: 
    for key in hit_list: 
        record.pop(key, None) 

# --- TASK 4: Verification ---
print("Verification - Cleaned Record:", new_data[0]) 

# --- TASK 5: Export ---
with open('lab3_cleaned_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["age", "zip_code", "salary"]) 
    writer.writeheader()
    writer.writerows(new_data)

print("\nSuccess: 'lab3_cleaned_data.csv' has been created.")