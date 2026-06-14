def mask_sensitive_data(input_str, mask_char='X'):
    
    parts = input_str.split('-')
    
    masked_parts = []
    for part in parts:
        if len(part) <= 4:
            
            masked_parts.append(mask_char * len(part))
        else:
            
            unmasked_part = part[-4:]
            masked_part = mask_char * (len(part) - 4) + unmasked_part
            masked_parts.append(masked_part)
    
    
    return '-'.join(masked_parts)



credit_card = "4532-8812-9001-4321"
masked_card = mask_sensitive_data(credit_card)
print(f"Original: {credit_card}")
print(f"Masked:   {masked_card}")


phone_number = "123-456-7890"
masked_phone = mask_sensitive_data(phone_number)
print(f"\nOriginal: {phone_number}")
print(f"Masked:   {masked_phone}")


print(f"\nMasked with *: {mask_sensitive_data(credit_card, '*')}")