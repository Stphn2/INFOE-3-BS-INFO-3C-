def mask_data(data_string, mask_char="X"):
    # Step 1: Split the string into a list [cite: 8, 13]
    parts = data_string.split("-") # Fill in the target character

    # Step 2: Loop through the list (except the last item) [cite: 12, 16]
    # len(parts) - 1 ensures we don't overwrite the final 4 digits
    for i in range(len(parts) - 1):
        
        # Constraint A: Work with 'X' or '*' [cite: 24]
        # Hint: In Python, you can multiply a string by an integer to repeat it.
        # Example: "X" * 4 becomes "XXXX"
        parts[i] = mask_char * len(parts[i])

    # Step 3: Join the list back together [cite: 17, 23]
    masked_string = "-".join(parts)

    return masked_string

# Validation Tests [cite: 27]
print(mask_data("4532-8812-9001-4321")) # Target: XXXX-XXXX-XXXX-4321 [cite: 6, 7]
print(mask_data("123-456-7890"))        # Target: XXX-XXX-7890 [cite: 29, 31]