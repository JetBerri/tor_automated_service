import os
import json
from colorama import Fore, Style, init

init(autoreset=True)

TORRC_PATH = "/etc/tor/torrc"
JSON_FILE_PATH = "tor_config.json"

def configure_torrc(address, port):
    try:
        with open(TORRC_PATH, 'r') as torrc_file:
            torrc_content = torrc_file.readlines()

        with open(TORRC_PATH, 'w') as torrc_file:
            for line in torrc_content:
                if line.startswith("HiddenServiceDir") or line.startswith("HiddenServicePort"):
                    # Uncomment the lines related to Hidden Service
                    torrc_file.write(line[1:])
                else:
                    torrc_file.write(line)

            # Add new Hidden Service configuration
            torrc_file.write(f"\nHiddenServiceDir /var/lib/tor/hidden_service/\n")
            torrc_file.write(f"HiddenServicePort 80 {address}:{port}\n")

        print(f"{Fore.GREEN}Tor configuration updated successfully.{Style.RESET_ALL}")

        # Write IP and Port to JSON file
        tor_config = {"address": address, "port": port}
        with open(JSON_FILE_PATH, 'w') as json_file:
            json.dump(tor_config, json_file, indent=4)

        print(f"{Fore.GREEN}IP and Port written to {JSON_FILE_PATH}.{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{Fore.RED}Tor configuration file not found. Please check the Tor installation.{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}Configure Tor Hidden Service in torrc file.{Style.RESET_ALL}")

    # Get user input for address and port
    address = input(f"{Fore.CYAN}Enter the address (e.g., 127.0.0.1): {Style.RESET_ALL}")
    port = input(f"{Fore.CYAN}Enter the port (e.g., 8080): {Style.RESET_ALL}")

    configure_torrc(address, port)

if __name__ == "__main__":
    main()