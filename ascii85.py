#!/usr/bin/env python3


import sys

def encode_ascii85(data):
    padding = (4 - len(data) % 4) % 4
    data += b'\x00' * padding

    encoded = []
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        num = int.from_bytes(chunk, byteorder='big')

        if num == 0:
            encoded.append('z')
        else:
            chars = []
            for _ in range(5):
                chars.append(chr(num % 85 + 33))
                num //= 85
            encoded.append(''.join(reversed(chars)))

    result = ''.join(encoded)
    if padding:
        result = result[:-padding]

    return result


def decode_ascii85(encoded):
    encoded = encoded.replace('z', '!!!!!')

    padding = (5 - len(encoded) % 5) % 5
    encoded += 'u' * padding

    decoded = bytearray()
    for i in range(0, len(encoded), 5):
        chunk = encoded[i:i+5]
        num = 0
        for char in chunk:
            num = num * 85 + (ord(char) - 33)

        decoded.extend(num.to_bytes(4, byteorder='big'))
    if padding:
        decoded = decoded[:-padding]

    return bytes(decoded)



try:
    code = decode_ascii85 if sys.argv[1] == '-d' else encode_ascii85
    sys.stdout.buffer.write(code(sys.stdin.buffer.read()))
except Exception:
    pass
