import subprocess

interface = input ("enter interface > ")

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["iwconfig", interface, "mode", "monitor"])

while True:
    try:
        mac = input ("change mac address ? (y/n) > ")
    except ValueError:
        continue

    if mac == 'y':
        print("[+] Changing MAC address\n")
        subprocess.run(["macchanger", "-r", interface])
        break
    
    elif mac == 'n':
        print("[+] Exiting program ...\n")
        break
    else:
        print("[-] invalid argument\n")

subprocess.run(["iwconfig", interface])