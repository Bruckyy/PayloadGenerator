def convert_port_to_hex(port):
    hex_value = hex(port)

    little_endian = hex_value[2:]
    little_endian = r"\x"+r"\x".join([little_endian[i:i+2] for i in range(0, len(little_endian), 2)])  # On inverse les octets par paires
    return little_endian

def ip_to_hex(ip_address):
    # Split the IP address into octets
    octets = ip_address.split('.')
    
    # Convert each octet to hexadecimal and join them with '\x'
    hex_ip = ''.join([f'\\x{int(octet):02x}' for octet in octets])
    
    return hex_ip

def get_ip_and_mask(hex_ip):
    bytes = hex_ip.split(r"\x")
    mask = []
    ip_edited = []

    for i in range(0,len(bytes)):
        if bytes[i] == '00':
            mask.append('04')
            ip_edited.append('03')
        else:
            mask.append(bytes[i])
            ip_edited.append(bytes[i])
            

    return ( r"\x".join(ip_edited),r"\x".join(mask))