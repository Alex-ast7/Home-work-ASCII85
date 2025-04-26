#!/usr/bin/env python3


import sys

def encode_ascii85(data):
    padding = (4 - len(data) % 4) % 4
    data += b'\x00' * padding
    encoded = bytearray()
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        num = int.from_bytes(chunk, byteorder='big')

        if num == 0:
            encoded.append(ord('z'))
        else:
            chars = bytearray()
            for _ in range(5):
                chars.append(num % 85 + 33)
                num //= 85
            encoded.extend(reversed(chars))

    if padding:
        encoded = encoded[:-padding]

    return bytes(encoded)



def decode_ascii85(encoded):
    encoded = encoded.replace(b'z', b'!!!!!')

    padding = (5 - len(encoded) % 5) % 5
    encoded += b'u' * padding

    decoded = bytearray()
    for i in range(0, len(encoded), 5):
        chunk = encoded[i:i+5]
        num = 0
        for char in chunk:
            num = num * 85 + (char - 33)

        decoded.extend(num.to_bytes(4, byteorder='big'))
    if padding:
        decoded = decoded[:-padding]

    return bytes(decoded)



code = decode_ascii85 if sys.argv[1] == '-d' else encode_ascii85
sys.stdout.buffer.write(code(sys.stdin.buffer.read()))
