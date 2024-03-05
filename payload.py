class Payload:
    def __init__(self,platform):
        if platform == "linux":
            self.shellcode = r"\x48\x31\xc0\x48\x31\xdb\x48\x31\xc9\x48\x31\xff\x48\x31\xd2\x48\x31\xf6" # Base opcodes to xor all registers
        self.length = self.get_length()
        self.size = self.get_bytes_size()
        self.platform = platform
        # self.target_ip = "127.0.0.1"
        # self.target_port = 667

    def __str__(self):
        return f"Payload\nLength: {self.length} - {self.size} Bytes - Platform: {self.platform}\nShellcode: {self.shellcode}"

    def permut(self):
        print("TODO: Do permutations here")
        if self.platform == "linux":
            print("Do linux things")

    def get_length(self):
        return self.shellcode.count(r"\x")
    
    def get_bytes_size(self):
        return self.get_length()//2