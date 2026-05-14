card_number = "123-4561-7890"

parts = card_number.split("-")

for i in range(len(parts) - 1):
    parts[i] = "X" * len(parts[i])

masked = "-".join(parts)

print(masked)
