from PIL import Image

def string_to_binary(message: str) -> str:
    """
    From string message to binary string.
    parameters: message (str): The message we wish to convert to binary.
    Returns:The binary of the message.
    """
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    return binary_message
