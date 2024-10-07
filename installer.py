import os
import subprocess

# Function to ensure the correct Kali repository is set up
def setup_kali_repo():
    try:
        print("Setting up the Kali Linux repository...")
        repo_entry = "deb http://http.kali.org/kali kali-rolling main non-free contrib\n"
        
        # Check if the repo is already set
        with open("/etc/apt/sources.list", "r") as file:
            if repo_entry not in file.read():
                with open("/etc/apt/sources.list", "a") as file_append:
                    file_append.write(repo_entry)
                print("Kali rolling repository added.")
            else:
                print("Kali rolling repository already present.")
        
        # Add the archive key
        subprocess.run(
            ['wget', '-q', '-O', '-', 'https://archive.kali.org/archive-key.asc', '|', 'sudo', 'apt-key', 'add'],
            check=True, shell=True
        )
        
        # Update package list
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        print("Package list updated.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set up repository: {e}")
        return False
    return True

# List of tools to install (GNOME Desktop Environment is excluded for now)
tools = [
    "aircrack-ng", "hydra", "metasploit-framework", "nmap", "john", "wireshark", "burpsuite",
    "sqlmap", "armitage", "ettercap-graphical", "nikto", "set", "maltego", "reaver", 
    "skipfish", "hashcat", "beef-xss", "kismet", "autopsy", "fern-wifi-cracker", 
    "exploitdb", "owasp-zap", "wifite", "apktool", "dirbuster", "yersinia", 
    "thc-hydra", "binwalk", "netcat", "dsniff", "unicornscan", "airodump-ng", 
    "airbase-ng", "airdecap-ng", "netdiscover", "recon-ng", "medusa", "cewl", 
    "xsser", "websploit", "snort", "sslstrip", "wifiphisher", "fluxion", 
    "powersploit", "responder", "volatility", "fimap", "evilginx", "lynis", 
    "radare2", "enum4linux", "arachni", "sqlninja", "wapiti", "golismero", 
    "hexinject", "dbeaver", "crunch", "patator", "gobuster", "thc-pptp-bruter", 
    "yara", "cewl", "bdfproxy", "wpscan", "dnschef", "w3af", "smbmap", 
    "hping3", "bed", "pack", "dotdotpwn", "braa", "msfconsole", "zphisher", 
    "cuckoo", "empire", "mimikatz", "ncat", "karmetasploit", "pixiewps", 
    "ophcrack", "crackmapexec", "pwntools", "thefatrat", "apktool", 
    "netsniff-ng", "dmitry", "koadic", "shellter", "theharvester", 
    "sublist3r", "enumiv", "xsstrike", "spade"
]

# Function to install a package using apt
def install_tool(tool):
    try:
        print(f"Installing {tool}...")
        subprocess.run(['sudo', 'apt', 'install', '-y', tool], check=True)
        print(f"{tool} installed successfully.\n")
    except subprocess.CalledProcessError:
        print(f"Failed to install {tool}. Continuing...\n")

# Main program
def main():
    # Ask the user if they want to install the GNOME Desktop Environment
    install_gnome = input("Do you want to install the GNOME Desktop Environment? (y/n): ").strip().lower()
    
    # List of GNOME packages
    gnome_tools = ["gnome-core", "gnome-terminal"]
    
    # Set up Kali repo first
    if setup_kali_repo():
        # If user chose 'y', install GNOME packages
        if install_gnome == 'y':
            for gnome_tool in gnome_tools:
                install_tool(gnome_tool)
            print("GNOME Desktop Environment installation complete.\n")
        else:
            print("Skipping GNOME Desktop Environment installation.\n")
        
        # Proceed to install the other tools
        for tool in tools:
            install_tool(tool)
        
        print("All installations complete.")
    else:
        print("Kali repo setup failed. Cannot proceed with installations.")

if __name__ == "__main__":
    main()
