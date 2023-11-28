# This uses the PyJWT library to try and decode JSON Web Tokens
# This was written because decoding it manually using something like CyberChef became frustrating, so I wanted a script that did it for me. 

import jwt
import sys

def decode_jwt(token):
    try:
        # Decode the JWT token without verifying the signature
        decoded_data = jwt.decode(token, algorithms=['HS256'], verify=False)
        
        # Print the decoded information
        print("Decoded JWT Data:")
        for key, value in decoded_data.items():
            print(f"{key}: {value}")
        
    except jwt.ExpiredSignatureError:
        print("Error: JWT Signature has expired.")
    except jwt.InvalidTokenError:
        print("Error: Invalid JWT token.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Prints syntax/usage instructions
    if len(sys.argv) != 2:
        print("Usage: python JWTDecoder.py <jwt_token>")
        sys.exit(1)

    jwt_token = sys.argv[1]

    # Call the function to decode and analyze the JWT
    decode_jwt(jwt_token)
