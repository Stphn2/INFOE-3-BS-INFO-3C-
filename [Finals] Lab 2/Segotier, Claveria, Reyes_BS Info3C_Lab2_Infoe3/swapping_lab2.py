import random
import pandas as pd
import copy

print("              PRE-SWAP METRICS")

# Load the data
df = pd.read_csv('employee_data.csv')
raw_data = df.to_dict('records')

# Calculate Pre-Swap Metrics
original_salaries = [record['salary'] for record in raw_data]
pre_swap_total = sum(original_salaries)
pre_swap_avg = pre_swap_total / len(original_salaries)

print(f"Total Payroll: ${pre_swap_total:,.2f}")
print(f"Average Salary: ${pre_swap_avg:,.2f}")
print("=" * 60)

# Display sample of original data (first 3 records)
print("\nSAMPLE OF ORIGINAL DATA (Before Swap):")
for i in range(min(3, len(raw_data))):
    print(f"  {raw_data[i]['name']} - ${raw_data[i]['salary']:,.2f}")


# Extract salaries into a separate list
salary_list = [record['salary'] for record in raw_data]


def safe_shuffle(salary_list, original_salaries):
    shuffled = salary_list.copy()
    random.shuffle(shuffled)
    
    shuffle_attempts = 1
    while True:
        # Check if any person got their original salary
        any_same = False
        for i in range(len(shuffled)):
            if shuffled[i] == original_salaries[i]:
                any_same = True
                break
        
        if not any_same:
            break
        

        random.shuffle(shuffled)
        shuffle_attempts += 1
    
    return shuffled



shuffled_salaries = safe_shuffle(salary_list, original_salaries)

# Re-inject the shuffled salaries
swapped_data = copy.deepcopy(raw_data)
for i, record in enumerate(swapped_data):
    record['salary'] = shuffled_salaries[i]



print("\n" + "=" * 60)
print("             POST-SWAP METRICS")

# Calculate Post-Swap Metrics
post_swap_total = sum([record['salary'] for record in swapped_data])
post_swap_avg = post_swap_total / len(swapped_data)

print(f"Total Payroll: ${post_swap_total:,.2f}")
print(f"Average Salary: ${post_swap_avg:,.2f}")
print("=" * 60)

# Display sample of swapped data (first 3 records)
print("\nSAMPLE OF SWAPPED DATA (After Swap):")
for i in range(min(3, len(swapped_data))):
    print(f"  {swapped_data[i]['name']} - ${swapped_data[i]['salary']:,.2f}")


# Export to new CSV
swapped_df = pd.DataFrame(swapped_data)
swapped_df.to_csv('swapped_employee_data.csv', index=False, encoding='utf-8-sig')

print("\n✅ Swapped dataset saved to 'swapped_employee_data.csv'")
