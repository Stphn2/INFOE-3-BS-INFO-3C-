import csv
import copy

# List for original data
raw_data = []

# Load the CSV file
with open("employee_data.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        raw_data.append(row)

# Create a deep copy of the data
new_data = copy.deepcopy(raw_data)

# Categorize age into life stages
for record in new_data:
    age = int(record["age"])

    if age < 30:
        record["age"] = "Under 30"

    elif age <= 50:
        record["age"] = "30 to 50"

    else:
        record["age"] = "Over 50"

    

# Generalize zip code
for record in new_data:
    zip_code = record["zip_code"]
    record["zip_code"] = zip_code[:3] + "XX"

# Print BEFORE and AFTER
print("BEFORE:")
print(raw_data[0])

print("\nAFTER:")
print(new_data[0])

# Verify average salary
total_salary = 0

for record in new_data:
    total_salary += int(record["salary"])

average_salary = total_salary / len(new_data)

print("\nAverage Salary:", average_salary)

# Export generalized data
with open("generalized_employee_data.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = new_data[0].keys()

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(new_data)

print("\nGeneralized CSV file created successfully.")