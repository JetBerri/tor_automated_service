# Automated Tor Service Launcher

This project provides a set of Python scripts to automate the setup and launch of a Tor service. The project consists of three main scripts:

1. `runcmd.py`: A utility module for running shell commands and capturing their output.
2. `server_execution.py`: A script that sets up a basic HTTP server with Tor-related functionalities.
3. `torrc.py`: A script to configure the Tor service by downloading a custom torrc configuration file.

## Instructions

### runcmd.py

This script, `runcmd.py`, is a utility module that simplifies the process of running shell commands. To use this module, include it in your Python script and call the `run_cmd` function.

Example usage:

```python
from runcmd.runcmd import run_cmd

# Run a command and print the output
status, stdout, stderr = run_cmd("ls -l", verbose=True)
print(f"Status: {status}")
print(f"Standard Output: {stdout}")
print(f"Standard Error: {stderr}")
```

**server_execution.py**

This script, `server_execution.py`, sets up a basic HTTP server with Tor-related functionalities. It logs server events to a specified file and provides an error handler for custom error messages. It also attempts to restart the Tor service upon termination.

Modify the following variables as needed:

```python
PORT: Port number for the HTTP server.
IP: IP address for the server.
LOG_FILE: File to store server logs.
```

**torrc.py**

This script, torrc.py, is responsible for configuring the Tor service. It checks if the user has superuser privileges, then downloads a custom torrc configuration file and saves it to /etc/tor/torrc. The script provides colored output for success and error messages.

Modify the following variables as needed:

```python
RED, GREEN, END_COLOR: ANSI color codes for colored output.
check_superuser: Function to check superuser privileges and configure Tor.
```

Example usage:

```
result, output = check_superuser()

if result:
    if output:
        # Additional actions with the output
else:
    print_colored("Operation could not be completed.", RED)

```

Feel free to adjust the formatting or add any additional details as necessary.

**Notes**

- Ensure you have the required permissions and dependencies installed to execute the scripts.
- Verify the Tor download URL in `installation.c` to match the latest Tor version.
- Review and adapt the code according to your specific use case and security requirements.
