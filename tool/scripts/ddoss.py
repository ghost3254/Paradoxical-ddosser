import colorama
import time
from colorama import Fore, Back, Style
ip = input("Enter IP address: ")
packets = input("How many packets to send: ")
packet_size = input("How large should the packets be in kb: ")
for i in range(int(packets)):
    print(Fore.RED + f"SENT {packet_size}KB TO {ip}")
    time.sleep(.01)