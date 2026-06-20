import csv
import copy

def load_raw_data(filename="GlobalCorp_PrivacyCleaned.csv"):
    raw_data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric fields for proper processing
            row['age'] = int(row['age'])
            row['salary'] = int(row['salary'])
            raw_data.append(row)
    return raw_data

raw_data = load_raw_data("GlobalCorp_PrivacyCleaned.csv")

generalized_data = copy.deepcopy(raw_data)

def generalize_age(age):
    """Round down age to the start of its decade"""
    return (age // 10) * 10

def generalize_zipcode(zip_code):
    """Keep first 3 characters, replace last 2 with XX"""
    zip_str = str(zip_code)
    return zip_str[:3] + "XX"

for record in generalized_data:
    record['age'] = generalize_age(record['age'])
    record['zip_code'] = generalize_zipcode(record['zip_code'])

print("=" * 50)
print("VERIFICATION: Before vs After Generalization")
print("=" * 50)
print(f"Original first record:  Age={raw_data[0]['age']}, Zip={raw_data[0]['zip_code']}")
print(f"Generalized first record: Age={generalized_data[0]['age']}, Zip={generalized_data[0]['zip_code']}")
print("=" * 50)


all_ages_end_in_zero = all(record['age'] % 10 == 0 for record in generalized_data)
print(f"\n✓ All ages end in 0: {all_ages_end_in_zero}")

all_zips_formatted = all(len(str(record['zip_code'])) == 5 and 
                          str(record['zip_code'])[:3].isdigit() and 
                          str(record['zip_code'])[3:] == "XX" 
                          for record in generalized_data)
print(f"✓ All zip codes follow 123XX format: {all_zips_formatted}")

def calculate_average_salary(data):
    total = sum(record['salary'] for record in data)
    return total / len(data)

original_avg_salary = calculate_average_salary(raw_data)
generalized_avg_salary = calculate_average_salary(generalized_data)

print(f"✓ Original Average Salary: ${original_avg_salary:,.2f}")
print(f"✓ Generalized Average Salary: ${generalized_avg_salary:,.2f}")
print(f"✓ Salaries match: {original_avg_salary == generalized_avg_salary}")

output_file = "GlobalCorp_Generalized.csv"

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = generalized_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(generalized_data)

print(f"\n✅ Exported generalized data to: {output_file}")

print("\n" + "=" * 50)
print("PREVIEW: First 5 Generalized Records")
print("=" * 50)
for i in range(min(5, len(generalized_data))):
    print(f"Record {i+1}: Age={generalized_data[i]['age']}, "
          f"Zip={generalized_data[i]['zip_code']}, "
          f"Salary=${generalized_data[i]['salary']:,}")
