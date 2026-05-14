def mask_data(input_string):
    parts = input_string.split("-")
    
    for i in range(len(parts) - 1):
        parts[i] = "X" * len(parts[i])
    
    return "-".join(parts)


print(mask_data("4532-8812-9001-4321")) 
print(mask_data("123-456-7890"))        