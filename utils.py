def convert_port_to_little_endian(port):
    hex_value = hex(port)

    little_endian = hex_value[2:]
    little_endian = r"\x"+r"\x".join([little_endian[i:i+2] for i in range(0, len(little_endian), 2)])  # On inverse les octets par paires
    return little_endian