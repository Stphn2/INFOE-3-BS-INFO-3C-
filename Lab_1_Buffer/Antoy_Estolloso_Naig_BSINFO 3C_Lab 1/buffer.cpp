#include <iostream>
#include <cstring>

int main() {
    
    char secret_key[16] = "TOP_SECRET_123";
    char password_buffer[8];

    std::cout << "--- Login ---" << std::endl;
    std::cout << "Enter 4-digit PIN: ";


    std::cin >> password_buffer; 

    if (strcmp(password_buffer, "1234") == 0) {
        std::cout << "Access Granted! Secret Key: " << secret_key << std::endl;
    } else {
        std::cout << "Access Denied." << std::endl;
        
        std::cout << "Current Memory State of Secret: " << secret_key << std::endl;
    }

    return 0;
}