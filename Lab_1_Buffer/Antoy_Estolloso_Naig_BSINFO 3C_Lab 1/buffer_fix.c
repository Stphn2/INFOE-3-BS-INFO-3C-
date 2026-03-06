#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    
    char secret_key[16] = "TOP_SECRET_123";
    char password_buffer[8];

    printf("--- Login ---\n");
    printf("Enter 4-digit PIN: ");

    if (fgets(password_buffer, sizeof(password_buffer), stdin) != NULL) {

        password_buffer[strcspn(password_buffer, "\n")] = '\0';

        if (strlen(password_buffer) == 4) {
            int valid = 1;
            for (int i = 0; i < 4; i++) {
                if (!isdigit(password_buffer[i])) {
                    valid = 0;
                    break;
                }
            }

            if (valid && strcmp(password_buffer, "1234") == 0) {
                printf("Access Granted! Secret Key: %s\n", secret_key);
                return 0;
            }
        }

        printf("Access Denied.\n");
    }

    return 0;
}