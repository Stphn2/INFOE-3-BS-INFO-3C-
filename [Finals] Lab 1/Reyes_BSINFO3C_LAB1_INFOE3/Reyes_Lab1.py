card_number = "4532-8812-9001-4321"

parts = card_number.split("-")

for i in range(len(parts) - 1):
    parts[i] = "****"

masked_card = "-".join(parts)

print("Original Card Number:", card_number)
print("Masked Card Number:", masked_card)

phone_number = "123-456-7890"
phone_parts = phone_number.split("-")

for i in range(len(phone_parts) - 1):
    phone_parts[i] = "***"

masked_phone = "-".join(phone_parts)

print("\nOriginal Phone Number:", phone_number)
print("Masked Phone Number:", masked_phone)