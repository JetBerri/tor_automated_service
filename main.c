#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to execute a Python script and handle errors

void executeScript(const char *scriptName) {

    printf("Executing script: %s\n", scriptName);

    // Construct the command to execute the Python script

    char command[256];
    snprintf(command, sizeof(command), "python3 %s", scriptName);

    // Use popen to execute the command and capture the output

    FILE *fp = popen(command, "r");
    if (fp == NULL) {
        fprintf(stderr, "Error opening pipe for %s\n", scriptName);
        exit(EXIT_FAILURE);
    }

    // Read the output of the command

    char buffer[128];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    // Close the pipe

    if (pclose(fp) != 0) {
        fprintf(stderr, "Error executing %s\n", scriptName);
        exit(EXIT_FAILURE);
    }

    printf("Script executed successfully: %s\n", scriptName);
}

// Function to handle errors and exit

void handleError(const char *errorMessage) {

    fprintf(stderr, "\x1b[31mError: %s\x1b[0m\n", errorMessage);
    exit(EXIT_FAILURE);
    
}

int main() {

    // Execute installation.py

    system("./installation");

    // Execute torrc.py

    executeScript("torrc.py");

    // Execute server_execution.py

    executeScript("server_execution.py");

    return 0;
}