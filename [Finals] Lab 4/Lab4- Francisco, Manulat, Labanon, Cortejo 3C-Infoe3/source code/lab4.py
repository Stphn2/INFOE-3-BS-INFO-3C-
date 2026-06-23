import csv
import copy

# 1. Load original data
raw_data = []
with open('employee_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        raw_data.append(row)

# 2. Process data for generalization
new_data = copy.deepcopy(raw_data)
total_salary = 0

for record in new_data:
    total_salary += float(record["salary"])
    
    # --- UPDATED FOR SS3: Life Stages Logic ---
    age = int(record["age"])
    if age < 30:
        record["age"] = "Under 30"
    elif age <= 50:
        record["age"] = "30 to 50"
    else:
        record["age"] = "Over 50"

    # Zip Code Generalization: Mask last 2 digits
    record["zip_code"] = record["zip_code"][:3] + "XX"
    # ------------------------------------------

# 3. Print Comparison (Matches the text-based sample)
print("BEFORE:")
print(raw_data[0])

print("\nAFTER:")
print(new_data[0])

print(f"\nAverage Salary: {total_salary / len(new_data)}")
print("\nGeneralized CSV file created successfully.")

# 4. Export to file
keys = new_data[0].keys()
with open('generalized_employee_data.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(new_data)