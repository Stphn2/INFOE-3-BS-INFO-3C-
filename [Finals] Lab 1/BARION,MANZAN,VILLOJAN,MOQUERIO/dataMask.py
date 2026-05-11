def mask_data(input_string, mask_char="X"):
    parts = input_string.split('-')

    masked_list = []
    for i in range(len(parts)):
        if i == len(parts) - 1:
            masked_list.append(parts[i])
        else:
            masked_list.append(mask_char * len(parts[i]))


    return "-".join(masked_list)

cc_input = "4532-8812-9001-4321"
print(f"Input:  {cc_input}")
print(f"Output: {mask_data(cc_input)}")