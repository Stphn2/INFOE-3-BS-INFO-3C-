import pandas as pd
import random

# Load the data generated from the first script
df = pd.read_csv('employee_data.csv')
raw_data = df.to_dict('records')

# 1. Calculate Pre-Swap Metrics [cite: 247]
original_salaries = [record['salary'] for record in raw_data]
pre_swap_total = sum(original_salaries)
pre_swap_avg = pre_swap_total / len(original_salaries)

print("=" * 60)
print("           PRE-SWAP METRICS")
print(f"Total Payroll: ${pre_swap_total:,.2f}")
print(f"Average Salary: ${pre_swap_avg:,.2f}")
print("=" * 60)

# === STEP A: DISPLAY SAMPLE BEFORE SWAPPING [cite: 192-194] ===
print("\nSAMPLE OF ORIGINAL DATA (Before Swap):")
for i in range(min(3, len(raw_data))):
    name = raw_data[i]['name']
    salary = raw_data[i]['salary']
    print(f" {name} - ${salary:,.2f}")
print("-" * 60)

# 2. Safe Shuffle Logic [cite: 261, 264-267]
def safe_shuffle(salary_list, originals):
    shuffled = salary_list.copy()
    random.shuffle(shuffled)
    # Loop until NO person has their original salary [cite: 267]
    while True:
        any_same = False
        for i in range(len(shuffled)):
            if shuffled[i] == originals[i]:
                any_same = True
                break
        if not any_same:
            break
        random.shuffle(shuffled)
    return shuffled

# Execute the swap [cite: 248]
shuffled_salaries = safe_shuffle(original_salaries, original_salaries)

# 3. Re-inject the shuffled salaries back into the raw_data [cite: 263]
for i in range(len(raw_data)):
    raw_data[i]['salary'] = shuffled_salaries[i]

# 4. Verify Integrity (Post-Swap Metrics) [cite: 249]
post_swap_total = sum(shuffled_salaries)
post_swap_avg = post_swap_total / len(shuffled_salaries)

print("\n" + "=" * 60)
print("           POST-SWAP METRICS")
print(f"Total Payroll: ${post_swap_total:,.2f}")
print(f"Average Salary: ${post_swap_avg:,.2f}")
print("=" * 60)

# === STEP B: DISPLAY SAMPLE AFTER SWAPPING [cite: 216-218] ===
print("\nSAMPLE OF SWAPPED DATA (After Swap):")
for i in range(min(3, len(raw_data))):
    name = raw_data[i]['name']
    salary = raw_data[i]['salary']
    print(f" {name} - ${salary:,.2f}")
print("-" * 60)

# 5. Export the final anonymized dataset [cite: 251]
df_swapped = pd.DataFrame(raw_data)
df_swapped.to_csv("swapped_employee_data.csv", index=False)
print("\n✔ Swapped dataset saved to 'swapped_employee_data.csv'")