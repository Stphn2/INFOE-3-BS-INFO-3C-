import csv
import copy

def load_raw_data(filename="anonymized_hr_data.csv"):
    raw_data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_data.append(row)
    return raw_data

raw_data = load_raw_data("anonymized_hr_data.csv")

new_data = copy.deepcopy(raw_data)

hit_list = ["name", "medical_risk"]

for record in new_data:
    for key in hit_list:
        record.pop(key, None)  

print("First cleaned record:")
print(new_data[0])

output_file = "GlobalCorp_PrivacyCleaned.csv"
if new_data:
    # Get remaining fieldnames from the first cleaned record
    fieldnames = list(new_data[0].keys())
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_data)
    
    print(f"\nExported cleaned data to {output_file}")
    print(f"Columns remaining: {fieldnames}")
else:
    print("No data to export.")
