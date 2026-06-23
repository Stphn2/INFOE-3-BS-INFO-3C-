def mask_data(data_string, mask_char="X"):
    parts = data_string.split("-")

    for i in range(len(parts) - 1):
        
        parts[i] = mask_char * len(parts[i])

    masked_string = "-".join(parts)

    return masked_string

print(mask_data("4532-8812-9001-4321"))
print(mask_data("123-456-7890"))