#include <iostream>
#include <string>

int main() {
    
    
    std::string secret_key = "TOP_SECRET_123";
    
    
    std::string password_buffer; 

    std::cout << "--- Login ---" << std::endl;
    std::cout << "Enter 4-digit PIN: ";

   
    std::cin >> password_buffer; 

    
    if (password_buffer == "1234") {
        std::cout << "Access Granted! Secret Key: " << secret_key << std::endl;
    } else {
        std::cout << "Access Denied." << std::endl;
        
        
        std::cout << "Current Memory State of Secret: " << secret_key << std::endl;
    }

    return 0;
}