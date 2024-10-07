import os
import subprocess

# List of tools to install, including the GNOME desktop environment
tools = [
    "gnome-core", "gnome-terminal", "aircrack-ng", "hydra", "metasploit-framework", "nmap", 
    "john", "wireshark", "burpsuite", "sqlmap", "armitage", "ettercap-graphical", 
    "nikto", "set", "maltego", "reaver", "skipfish", "hashcat", "beef-xss", 
    "kismet", "autopsy", "fern-wifi-cracker", "exploitdb", "owasp-zap", "wifite", 
    "apktool", "dirbuster", "yersinia", "thc-hydra", "binwalk", "netcat", "dsniff", 
    "unicornscan", "airodump-ng", "airbase-ng", "airdecap-ng", "netdiscover", 
    "recon-ng", "medusa", "cewl", "xsser", "websploit", "snort", "sslstrip", 
    "wifiphisher", "fluxion", "powersploit", "responder", "volatility", "fimap", 
    "evilginx", "lynis", "radare2", "enum4linux", "arachni", "sqlninja", "wapiti", 
    "golismero", "hexinject", "dbeaver", "crunch", "patator", "gobuster", 
    "thc-pptp-bruter", "yara", "cewl", "bdfproxy", "wpscan", "dnschef", 
    "w3af", "smbmap", "hping3", "bed", "pack", "dotdotpwn", "braa", 
    "msfconsole", "zphisher", "cuckoo", "empire", "mimikatz", "ncat", 
    "karmetasploit", "pixiewps", "ophcrack", "crackmapexec", "pwntools", 
    "thefatrat", "apktool", "netsniff-ng", "dmitry", "koadic", "shellter", 
    "theharvester", "sublist3r", "enumiv", "xsstrike", "spade"
]

# Function to install a package using apt
def install_tool(tool):
    try:
        print(f"Installing {tool}...")
        subprocess.run(['sudo', 'apt', 'install', '-y', tool], check=True)
        print(f"{tool} installed successfully.\n")
    except subprocess.CalledProcessError:
        print(f"Failed to install {tool}. Continuing...\n")

# Iterate over the list and install each tool
for tool in tools:
    install_tool(tool)

print("All installations complete.")
