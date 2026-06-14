import random
import csv
from faker import Faker

fake = Faker()


def generate_raw_data(num_entries=30):
    raw_data = []
    medical_risk_options = ["Low", "Medium", "High"]
    
    for _ in range(num_entries):
        entry = {
            "name": fake.name(),
            "age": random.randint(22, 65),
            "zip_code": fake.zipcode()[:5],  
            "salary": random.randint(40000, 150000),
            "medical_risk": random.choice(medical_risk_options)
        }
        raw_data.append(entry)
    return raw_data


def calculate_metrics(data):
    salaries = [entry["salary"] for entry in data]
    total = sum(salaries)
    average = total / len(salaries) if salaries else 0
    return total, average


def swap_salaries(data):
    
    salaries = [entry["salary"] for entry in data]
    
    random.shuffle(salaries)
    
    for i, entry in enumerate(data):
        entry["salary"] = salaries[i]
    
    return data


def swap_with_safety_check(original_data):
    
    original_salaries = [entry["salary"] for entry in original_data]
    
    swapped_data = swap_salaries(original_data.copy())
    
    
    same_salary_count = sum(
        1 for i, entry in enumerate(swapped_data)
        if entry["salary"] == original_salaries[i]
    )
    
    
    while same_salary_count > 0:
        swapped_data = swap_salaries(original_data.copy())
        same_salary_count = sum(
            1 for i, entry in enumerate(swapped_data)
            if entry["salary"] == original_salaries[i]
        )
    
    return swapped_data


def export_to_csv(data, filename="anonymized_data.csv"):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"✅ Exported to {filename}")


if __name__ == "__main__":
    print("🔹 Generating raw dataset...")
    raw_data = generate_raw_data(30)  
    
    
    pre_total, pre_avg = calculate_metrics(raw_data)
    print(f"\n📊 Pre-Swap Metrics:")
    print(f"   Total Payroll: ${pre_total:,.2f}")
    print(f"   Average Salary: ${pre_avg:,.2f}")
    
    
    print("\n🔄 Swapping salaries...")
    anonymized_data = swap_with_safety_check(raw_data)
    
    
    post_total, post_avg = calculate_metrics(anonymized_data)
    print(f"\n📊 Post-Swap Metrics:")
    print(f"   Total Payroll: ${post_total:,.2f}")
    print(f"   Average Salary: ${post_avg:,.2f}")
    
    
    print("\n🔍 Integrity Check:")
    print(f"   Total Match: {'✅' if pre_total == post_total else '❌'}")
    print(f"   Average Match: {'✅' if pre_avg == post_avg else '❌'}")
    
    
    export_to_csv(anonymized_data, "anonymized_hr_data.csv")
    
    
    print("\n📋 Preview of anonymized data (first 3 rows):")
    for i in range(min(3, len(anonymized_data))):
        print(anonymized_data[i])
