import random
import csv
from faker import Faker

fake = Faker()
raw_data = []
for _ in range(30):
    entry = {
        'name': fake.name(),
        'age': random.randint(22, 75),
        'zip_code': fake.zipcode(),
        'salary': random.randint(40000, 160000),
        'medical_risk': random.choice(["Low", "Medium", "High"])
    }
    raw_data.append(entry)

pre_total = sum(d['salary'] for d in raw_data)
pre_avg = pre_total / len(raw_data)
print(f"Pre-Swap: Total={pre_total}, Average={pre_avg}")

original_salaries = [d['salary'] for d in raw_data] # [cite: 34]
shuffled_salaries = original_salaries.copy()

while True:
    random.shuffle(shuffled_salaries)
    if shuffled_salaries != original_salaries:
        break

for i in range(len(raw_data)):
    raw_data[i]['salary'] = shuffled_salaries[i]


post_total = sum(d['salary'] for d in raw_data)
post_avg = post_total / len(raw_data)
print(f"Post-Swap: Total={post_total}, Average={post_avg}")

keys = raw_data[0].keys()  
with open('anonymized_data.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(raw_data)

print("Anonymized dataset saved to 'anonymized_data.csv'.")