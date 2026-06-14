import random
import csv
import copy
from faker import Faker

# --- Consistency Seeds ---
random.seed(42)
Faker.seed(42)

fake = Faker()

# --- TASK 1: Load the Data ---
raw_data = []
for _ in range(30):
    raw_data.append({
        "name": fake.name(),
        "age": random.randint(18, 75),
        "zip_code": fake.zipcode(),
        "salary": random.randint(30000, 150000),
        "medical_risk": random.choice(["Low", "Medium", "High"])
    })

# APPLY LAB 2 SWAP: Maintain the "Anonymized" baseline from Lab 2
swapped_salaries = [record["salary"] for record in raw_data]
random.shuffle(swapped_salaries)
while swapped_salaries[0] == raw_data[0]["salary"]:
    random.shuffle(swapped_salaries)
for i in range(len(raw_data)):
    raw_data[i]["salary"] = swapped_salaries[i]

# --- PRE-GENERALIZATION METRIC ---
avg_salary_lab2 = sum(r['salary'] for r in raw_data) / len(raw_data)

# --- TASK 1: Load Data ---
gen_data = copy.deepcopy(raw_data)
before_record = copy.deepcopy(gen_data[0]) 

# --- TASK 2: Execute Generalization ---
for record in gen_data:
    # UPDATED: Categorize Age into "Life Stages" per image_a2e6f3.png
    age = record["age"]
    if age < 30:
        record["life_stage"] = "Under 30"
    elif 30 <= age <= 50:
        record["life_stage"] = "30 to 50"
    else:
        record["life_stage"] = "Over 50"
    
    # Remove the original age field to maintain privacy
    record.pop("age")
    
    # Generalize Zip Code
    record["zip_code"] = str(record["zip_code"])[:3] + "XX"

# --- TASK 3: Verification
print("--- Lab 4 Verification ---")
print(f"Before (Precise): {before_record}")
print(f"After (Generalized): {gen_data[0]}")

# Integrity Check: Prove the Average Salary still matches Lab 2 
avg_salary_lab4 = sum(r['salary'] for r in gen_data) / len(gen_data)
print("\n--- Salary Integrity Check ---")
print(f"Average Salary from Lab 2: {avg_salary_lab2:.2f}")
print(f"Average Salary in Lab 4:   {avg_salary_lab4:.2f}")
print(f"Integrity Match: {avg_salary_lab2 == avg_salary_lab4}")

# --- TASK 4: Export ---
with open('lab4_generalized_data.csv', 'w', newline='') as f:
    # Updated fieldnames to include "life_stage" instead of "age"
    fieldnames = ["name", "life_stage", "zip_code", "salary", "medical_risk"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(gen_data)

print("\nSuccess: 'lab4_generalized_data.csv' has been created.")