import os
import platform
import subprocess
import requests
import zipfile
import tarfile
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

TOR_BROWSER_LAUNCHER_URL = "https://github.com/micahflee/torbrowser-launcher/releases/download/v0.4.0/torbrowser-launcher-0.4.0_all.deb"
TOR_BROWSER_LAUNCHER_FILENAME = "torbrowser-launcher.deb"
TOR_INSTALLATION_CMD = "sudo apt install torbrowser-launcher -y"

TOR_SERVICE_INSTALLATION_CMD = {
    "Linux": "sudo apt install tor -y",
    "Windows": "choco install tor -y",  # Requires Chocolatey to be installed
    "Darwin": "brew install tor",  # Requires Homebrew to be installed
}

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)

def extract_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def extract_tar(tar_path, extract_path):
    with tarfile.open(tar_path, 'r') as tar_ref:
        tar_ref.extractall(extract_path)

def install_tor_browser_launcher():
    print(f"{Fore.CYAN}Downloading Tor Browser Launcher...{Style.RESET_ALL}")
    download_file(TOR_BROWSER_LAUNCHER_URL, TOR_BROWSER_LAUNCHER_FILENAME)

    print(f"{Fore.CYAN}Installing Tor Browser Launcher...{Style.RESET_ALL}")
    os.system(f"sudo dpkg -i {TOR_BROWSER_LAUNCHER_FILENAME}")
    os.system("sudo apt install -f -y")

def install_tor_service():
    system = platform.system()
    if system in TOR_SERVICE_INSTALLATION_CMD:
        print(f"{Fore.CYAN}Installing Tor service for {system}...{Style.RESET_ALL}")
        os.system(TOR_SERVICE_INSTALLATION_CMD[system])
    else:
        print(f"{Fore.RED}Tor service installation not supported for {system}.{Style.RESET_ALL}")

def main():
    try:
        tor_launcher_installed = subprocess.call(["torbrowser-launcher", "--version"])
    except FileNotFoundError:
        tor_launcher_installed = 1

    if tor_launcher_installed != 0:
        install_tor_browser_launcher()

    try:
        tor_service_installed = subprocess.call(["tor", "--version"])
    except FileNotFoundError:
        tor_service_installed = 1

    if tor_service_installed != 0:
        install_tor_service()

    print(f"{Fore.GREEN}Tor setup completed.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()