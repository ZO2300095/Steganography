import unittest
from PIL import Image
from steganography import *

class TestStringToBinary(unittest.TestCase):

    def test_hola(self):
        """Test binary conversion for the word 'Hola'."""
        message = "Hola"
        expected_binary = '01001000011011110110110001100001'  # Binary representation for "Hola"
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

    def test_empty_string(self):
        """Test the binary conversion for an empty string."""
        message = ""
        expected_binary = ""
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

    def test_long_sentence(self):
        """Test binary conversion for a longer sentence."""
        message = "Ziad Ahmed plays football at el Real Madrid"
        expected_binary = ''.join(format(ord(c), '08b') for c in message)
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

    def test_special_characters(self):
        """Test binary conversion for special characters and spaces."""
        message = "Attention, please !!"
        expected_binary = ''.join(format(ord(c), '08b') for c in message)
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

    def setUp(self):
        """Create a simple 10x10 white test image."""
        self.test_image_path = 'test_image.png'
        self.test_output_path = 'test_output_image.png'
        img = Image.new('RGB', (10, 10), color=(255, 255, 255))
        img.save(self.test_image_path)

    def test_string_to_binary(self):
        """Test converting a basic string to binary."""
        message = "Hello"
        expected_binary = '0100100001100101011011000110110001101111'
        binary = string_to_binary(message)
        self.assertEqual(binary, expected_binary)

    def test_hide_message_in_image(self):
        """Test hiding a simple message in an image."""
        message = "Hi"
        hide_message_in_image(self.test_image_path, message, self.test_output_path)
        # Check if the output file was created
        self.assertTrue(Image.open(self.test_output_path))

    def test_extract_message_from_image(self):
        """Test extracting the hidden message from an image."""
        message = "Hi"
        hide_message_in_image(self.test_image_path, message, self.test_output_path)
        # Extract the hidden message from the image
        extracted_message = extract_message_from_image(self.test_output_path, len(string_to_binary(message)))
        self.assertEqual(extracted_message, message)

    def test_message_too_large(self):
        """Test that an error is raised when the message is too large for the image."""
        message = "This message is too large for the image." * 10  # Making the message too long
        with self.assertRaises(ValueError):
            hide_message_in_image(self.test_image_path, message, self.test_output_path)

    def test_empty_message(self):
        """Test that an error is raised if the message is empty."""
        message = ""
        with self.assertRaises(ValueError):
            hide_message_in_image(self.test_image_path, message, self.test_output_path)

if __name__ == '__main__':
    unittest.main()
