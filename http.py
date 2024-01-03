import http.server
import socketserver
import sys
import argparse
import json
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Custom HTTP Server")
    parser.add_argument("--port", type=int, help="Port for the HTTP server")
    parser.add_argument("--address", help="Address to bind the HTTP server")
    return parser.parse_args()

def read_tor_config():
    try:
        with open('tor_config.json', 'r') as json_file:
            tor_config = json.load(json_file)
        return tor_config.get("address", "127.0.0.1"), tor_config.get("port", 8080)
    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        return "127.0.0.1", 8080

def main():
    args = parse_arguments()

    # Set the desired port and address
    tor_address, tor_port = read_tor_config()
    port = args.port or tor_port
    address = args.address or tor_address

    try:
        # Redirect stdout to a file
        sys.stdout = open('log.log', 'w')

        # Create a custom handler to suppress log messages
        class QuietHandler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                pass

        # Create and configure the server
        with socketserver.TCPServer((address, port), QuietHandler) as httpd:
            print(Fore.GREEN + f"Serving on {address}:{port}")

            try:
                # Start the server
                httpd.serve_forever()
            except KeyboardInterrupt:
                # Handle keyboard interrupt to gracefully stop the server
                print(Fore.YELLOW + "\nServer stopped.")
            finally:
                # Close the log file
                sys.stdout.close()

    except Exception as e:
        print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    main()