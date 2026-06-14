import copy
import csv

raw_data = []

with open('employee_data.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['salary'] = int(row['salary'])  
        raw_data.append(row)


cleaned_data = copy.deepcopy(raw_data)

hit_list = ["name", "medical_risk"]


for record in cleaned_data:
    for key in hit_list:
        record.pop(key, None)  
print("{")
for key, value in cleaned_data[0].items():
    print(f"   {key}: {value}")
print("}")


with open('cleaned_employee_data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=['age', 'zip_code', 'salary'])
    writer.writeheader()
    writer.writerows(cleaned_data)

print("\n✅ Success! Final CSV has been saved!")