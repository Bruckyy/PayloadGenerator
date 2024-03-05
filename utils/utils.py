
def print_payload_size(shellcode):
    print("Payload size: " + str(shellcode.count(r"\x")))