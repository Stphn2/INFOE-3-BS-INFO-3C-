import hashlib
import os

# The file we want to protect
filename = "database.csv"

def get_file_hash(path):
    # Initialize the SHA-256 algorithm
    sha256_hash = hashlib.sha256()
    
    # Open the file in binary mode ('rb') to read raw data
    with open(path, "rb") as f:
        # Read the file in small chunks (4096 bytes) 
        # This prevents memory crashes if the file is very large
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    # Return the hexadecimal string representation of the hash
    return sha256_hash.hexdigest()

# Generate and print the result
try:
    if os.path.exists(filename):
        print(f"--- INTEGRITY INITIALIZATION ---")
        print(f"Target File: {filename}")
        
        # Calculate the hash
        file_fingerprint = get_file_hash(filename)
        
        print(f"SHA-256 Hash: {file_fingerprint}")
        print("-" * 30)
        print("above is your HASH, MASTER! ")    
    else:
        print(f"Error: '{filename}' not found. Please create the file first.")

except Exception as e:
    print(f"An error occurred: {e}")