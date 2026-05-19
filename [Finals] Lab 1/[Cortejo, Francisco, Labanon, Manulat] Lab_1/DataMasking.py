def mask_data(input_string):
    
    segments = input_string.split("-") 
    
    masked_list = []
    
    for i in range(len(segments)):
       
        if i == len(segments) - 1:
            masked_list.append(segments[i]) 
        else:
            masked_list.append("X" * len(segments[i])) 

    return "-".join(masked_list) 
    #return result

print("--- SecureBank Data Masking Utility ---")
print("1. Mask Credit Card")
print("2. Mask Phone Number")

choice = input("Select an option (1 or 2): ")

if choice == '1':
    user_input = input("Enter the Card Number (e.g., 4532-8812-9001-4321): ")
    print(f"Masked Card: {mask_data(user_input)}")
elif choice == '2':
    user_input = input("Enter the Phone Number (e.g., 123-456-7890): ")
    print(f"Masked Phone: {mask_data(user_input)}")
else:
    print("Invalid selection. Please run the program again.")

