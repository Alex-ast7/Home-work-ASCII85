#!/bin/bash

dd if=/dev/random bs=2K count=1 status=none of=random.bin

python3 -c 'import sys
import base64
sys.stdout.buffer.write(base64.a85encode(sys.stdin.buffer.read()))
' <random.bin >random.a85

./ascii85 -e <random.bin >random.a85.test
./ascii85 -d <random.a85 >random.bin.test

# Тестирование кодера
if ! cmp -s random.a85 random.a85.test; then
  echo Encoder failed on random data >&2
  exit 1
fi

# Тестирование декодера
if ! cmp -s random.bin random.bin.test; then
  echo Decoder failed on random data >&2
  exit 1
fi

# Если дошли до сюда, всё хорошо
echo Ok! >&2
exit 0
