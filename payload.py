from opcodes import permut_list
from random import randint

class Payload:
    def __init__(self,platform):
        self.shellcode = ""
        self.platform = platform
        self.arch = "x64"
        # self.target_ip = "127.0.0.1"
        # self.target_port = 667

    def __str__(self):
        return f"\nPlatform: {self.platform} {self.arch} - Length: {self.get_length()} - {self.get_bytes_size()} Bytes\nShellcode: {self.shellcode}"

    def permut(self):
        if self.platform == "Linux":
            for line in permut_list:
                    self.shellcode += line[randint(0,len(line)-1)]

    def get_length(self):
        return self.shellcode.count(r"\x")
    
    def get_bytes_size(self):
        return self.get_length()//2