import subprocess, os
from runcmd.runcmd import run_cmd

RED = '\033[91m'
GREEN = '\033[92m'
END_COLOR = '\033[0m'

def print_colored(message, color):

    print(color + message + END_COLOR)

def check_superuser():

    try:

        if os.getuid() != 0:

            msg = "[sudo] password for %u: "
            subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)

            status, stdout, stderr = run_cmd("sudo wget -O /etc/tor/torrc https://raw.githubusercontent.com/JetBerri/lazy-service/main/torrc_configuration/torrc?token=GHSAT0AAAAAACMOGICIHAIXADCAPSDB6QRAZNDCIHQ", verbose=True)

            if status == 0:

                print_colored("Status 200 OK", GREEN)
                print(stdout.strip())

                return "Status 200 OK", stdout.strip()
            
            else:
                
                return f"Error: {stderr.strip()}", None
        else:

            raise PermissionError("You do not have superuser privileges.")
        
    except subprocess.CalledProcessError as e:

        print_colored(f"Error running command: {e}", RED)
        print_colored(f"Error output: {e.stderr.strip()}", RED)

        return f"Error: {e.stderr.strip()}", None

result, output = check_superuser()

if result:

    if output:

        pass

else:
    
    print_colored("Operation could not be completed.", RED)