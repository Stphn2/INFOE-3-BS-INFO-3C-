import csv
import copy

# --- PART 1: LOAD THE DATA ---
# This matches the "Load the Data" task in your manual
raw_data = []
try:
    # Fixed the encoding syntax (used '=' instead of '-')
    with open('employee_data.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert salary to int as required by previous labs
            row['salary'] = int(row['salary'])
            raw_data.append(row)
except FileNotFoundError:
    print("Error: employee_data.csv not found. Please create it first!")

# --- PART 2: PROTECT ORIGINAL DATA ---
# Using deepcopy ensures the 'original evidence' is not destroyed
cleaned_data = copy.deepcopy(raw_data)

# --- PART 3: DEFINE THE HIT LIST ---
# These are the "Direct Identifiers" and "High-Risk" attributes
hit_list = ["name", "medical_risk"]

# --- PART 4: EXECUTE SUPPRESSION ---
# This nested loop removes the sensitive keys safely
for record in cleaned_data:
    for key in hit_list:
        # Fixed the .pop() syntax (added 'None' to prevent crashes)
        record.pop(key, None)

# --- PART 5: VERIFICATION ---
# Print one record to the terminal to show name and medical_risk are gone
if cleaned_data:
    print("Verification (First Record):")
    print(cleaned_data[0])

# --- PART 6: EXPORT ---
# Save as a new CSV with exactly 3 columns: age, zip_code, salary
with open('cleaned_employee_data.csv', 'w', newline='') as file:
    fieldnames = ['age', 'zip_code', 'salary']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(cleaned_data)

print("\nSuccess! Final CSV has been saved!")