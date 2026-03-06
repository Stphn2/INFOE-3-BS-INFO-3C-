# # cell 2
# import hashlib
# import os

# # STEP 1: The 'Protection Profile' 
# # You need the string from Cell 1 to know what "Safe" looks like.
# EXPECTED_HASH = "PASTE_YOUR_HASH_HERE"
# filename = 'database.csv'

# def run_integrity_audit():
#     # A. THE AVAILABILITY CHECK
#     # Use 'os.path.exists' to make sure the file hasn't been deleted.

#     # B. THE FINGERPRINTING
#     # Create a new sha256 object. 
#     # Open the file in 'rb' mode.
#     # Use a loop to '.update()' the hash with the file data.
#     # Convert the result to a '.hexdigest()'.
    
#     # C. THE TECHNICAL CONTROL
#     # Use 'if/else' to compare your new hash to the EXPECTED_HASH.
#     # What message should the Subject (the script) print if they match?
#     # What alert should it trigger if they don't?
#     pass

# # Run the function
# run_integrity_audit()

import hashlib
import os

# STEP 1: The 'Protection Profile' 
# This hash corresponds exactly to the content created in Step 1
EXPECTED_HASH = "2a40b9b24576133fe051e309212d8a215af28402fa93760fc7e4befd06236fb2"
filename = 'database.csv'

def run_integrity_audit():
    # A. THE AVAILABILITY CHECK
    if not os.path.exists(filename):
        print(f"[ALERT] Availability Error: '{filename}' not found! The file may have been deleted.")
        return

    # B. THE FINGERPRINTING
    sha256_hash = hashlib.sha256()
    
    try:
        with open(filename, "rb") as f:
            # Read in 4KB blocks to be memory efficient
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        current_hash = sha256_hash.hexdigest()
        
        # C. THE TECHNICAL CONTROL
        if current_hash == EXPECTED_HASH:
            print(f"[SUCCESS] Integrity Verified: '{filename}' has not been tampered.")
        else:
            print(f"[CRITICAL ALERT] Integrity Breach: '{filename}' has been TAMPERED! ")
            
    except Exception as e:
        print(f"[ERROR] Audit failed due to system error: {e}")

# Run the function
run_integrity_audit()