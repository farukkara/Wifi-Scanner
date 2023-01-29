import subprocess

def scan_wifi():
    # Run the command to scan for WiFi networks
    result = subprocess.run(['iwlist', 'wlan0', 'scan'], stdout=subprocess.PIPE)
    # Parse the output of the command
    lines = result.stdout.decode().split('\n')
    networks = []
    for line in lines:
        if 'ESSID' in line:
            networks.append(line.split(':')[1].strip())
    return networks

print(scan_wifi())
