# This can decode base64 encoded strings, which are pretty common in CTFs
# This is probably much easier when leveraging something like CyberChef, but I wanted to practice writing scripts

import base64

def base64_decode(encoded_str):
    decoded_str = base64.b64decode(encoded_str).decode('utf-8')
    return decoded_str
