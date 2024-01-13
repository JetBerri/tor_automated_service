#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#define TOR_URL "https://www.torproject.org/dist/torbrowser/13.0.8/tor-browser-linux-x86_64-13.0.8.tar.xz"
#define DOWNLOADS_FOLDER "/home/%s/Downloads"
#define TOR_FOLDER "tor-browser_en-US"

int main() 

    {
    
    // Check if Tor is already installed

    struct stat torCheck;
    if (stat(TOR_FOLDER, &torCheck) == 0) {
        printf("Tor is already installed.\n");
        return 0;

    }

    printf("Downloading Tor...\n");

    // Get the current username

    char *username = getenv("USER");

    if (username == NULL) 
    {
        fprintf(stderr, "Error: Could not retrieve the current username.\n");
        return 1;
    }

    // Create the Downloads folder if it doesn't exist

    char downloadsFolder[100];

    snprintf(downloadsFolder, sizeof(downloadsFolder), DOWNLOADS_FOLDER, username);

    if (access(downloadsFolder, F_OK) == -1) 
    {
        char mkdirCommand[150];
        snprintf(mkdirCommand, sizeof(mkdirCommand), "mkdir -p %s", downloadsFolder);
        system(mkdirCommand);
    }

    // Change directory to Downloads

    chdir(downloadsFolder);

    // Download the Tor browser bundle using wget

    if (system("wget " TOR_URL) != 0) 
    {
        fprintf(stderr, "Error: Failed to download Tor.\n");
        return 1;
    }

    printf("Extracting Tor...\n");

    // Extract the downloaded archive

    if (system("tar -xf tor-browser-linux64-10.5.6_en-US.tar.xz") != 0) 
    {
        fprintf(stderr, "Error: Failed to extract Tor.\n");
        return 1;
    }

    // Clean up downloaded files

    system("rm tor-browser-linux64-10.5.6_en-US.tar.xz");

    // Check if Tor is now installed

    if (stat(TOR_FOLDER, &torCheck) == 0) 
    {
        printf("Tor setup complete.\n");
        return 0;
    } else 
    {
        fprintf(stderr, "Error: Tor installation failed.\n");
        return 1;
    }
}