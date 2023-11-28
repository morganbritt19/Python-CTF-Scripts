# This will convert hexadecimal strings to ASCII
# This is probably easier with CyberChef, but I like practicing writing scripts

def hex_to_ascii(hex_str):
    ascii_str = bytes.fromhex(hex_str).decode('utf-8')
    return ascii_str
