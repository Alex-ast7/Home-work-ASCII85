import unittest
import base64
from ascii85 import encode_ascii85, decode_ascii85


class TestASCII85(unittest.TestCase):
    def test_encode_simple_string(self):
        """Тест: Кодирование простой строки"""
        data = b"Hello, World!"
        expected = base64.a85encode(data).decode('ascii')
        self.assertEqual(encode_ascii85(data), expected)

    def test_encode_with_padding(self):
        """Тест: Кодирование строки с padding"""
        data = b"Hello"
        expected = base64.a85encode(data).decode('ascii')
        self.assertEqual(encode_ascii85(data), expected)

    def test_decode_simple_string(self):
        """Тест: Декодирование строки <<St. Petersburg State University is the best of all>>"""
        data = ';fjW7:h=`[EcY]4Eb?LnFCB9&+B<;nG%G]8BlnVCBlbD=BOr;qATMr9De:,#Chs'
        expected = base64.a85decode(data)
        self.assertEqual(decode_ascii85(data), expected)

    def test_encode_decode_round_trip(self):
        """Тест: Кодирование и декодирование (обратимость)"""
        data = b"Test round trip!"
        encoded = encode_ascii85(data)
        decoded = decode_ascii85(encoded)
        self.assertEqual(decoded, data)

    def test_compare_with_base64_a85(self):
        """Тест: Сравнение с результатами base64.a85encode и base64.a85decode"""
        data = b"Hello, World!"

        ascii85_encoded = encode_ascii85(data)
        ascii85_decoded = decode_ascii85(ascii85_encoded)

        base64_encoded = base64.a85encode(data).decode('ascii')
        base64_decoded = base64.a85decode(base64_encoded)

        self.assertEqual(ascii85_encoded, base64_encoded)
        self.assertEqual(ascii85_decoded, base64_decoded)
        self.assertEqual(ascii85_decoded, data)


if __name__ == "__main__":
    unittest.main()
