#!/usr/bin/python3

import argparse
import subprocess
import sys

def get_argument():
    parser = argparse.ArgumentParser(add_help = False, usage='[interface] [mode]')
    parser.add_argument("-h ","--help", action = "help", help ='show this help message and exit')

    parser.add_argument('-i','--interface',metavar='',help='Specify your interface')
    parser.add_argument('-mon','--monitor',action='store_true',help='Into monitor mode')
    parser.add_argument('-man','--managed',action='store_true',help='Into managed mode')

    return parser.parse_args()


def monitor_mode():
    subprocess.run(["ifconfig", args.interface, "down"])
    subprocess.run(["iwconfig", args.interface, "mode", "monitor"])
    subprocess.run(["iwconfig", args.interface])
    print("[+] mon")

def managed_mode():
    subprocess.run(["iwconfig", args.interface, "mode", "managed"])
    subprocess.run(["ifconfig", args.interface, "up"])
    subprocess.run(["ifconfig", args.interface])
    print("[+] man")

args = get_argument()

if args.monitor:
    monitor_mode()
if args.managed:
    managed_mode()

#ip link set interface name new_interface
