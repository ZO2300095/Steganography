import unittest
from steganography import string_to_binary

class TestStringToBinary(unittest.TestCase):

    def test_hola(self):
        message = "Hola"
        expected_binary = '01001000011011110110110001100001'  # Expected binary
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

    def test_empty_string(self):
        message = ""
        expected_binary = "" # Expected binary
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

    def test_long_sentence(self):
        message = "Ziad Ahmed plays football at el Real Madrid"
        expected_binary = ''.join(format(ord(c), '08b') for c in message) # Expected binary
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

    def test_special_characters(self):
        message = "Attention, please !!"
        expected_binary = ''.join(format(ord(c), '08b') for c in message) # Expected binary
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

if __name__ == '__main__':
    unittest.main()
