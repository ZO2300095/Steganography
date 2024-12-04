from PIL import Image

def string_to_binary(message: str) -> str:
    """Convert the message to binary."""
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    return binary_message

def hide_message_in_image(image_path, message, output_path):
    """Hide the secret message in the image (using the LSB method)."""
    if not message:
        raise ValueError("Message cannot be empty!")  # Check if the message is empty
    
    # Open the image using Pillow
    image = Image.open(image_path)
    pixels = image.load()  # Access image pixels
    
    # Convert the message to binary and add an end-of-message marker
    binary_message = string_to_binary(message) + '1111111111111110'  # Marker for end of message
    message_length = len(binary_message)
    width, height = image.size
    
    # Check if the image can hold the message
    max_message_length = width * height * 3  # 3 channels (RGB)
    if message_length > max_message_length:
        raise ValueError(f"The message is too large for this image. Max size: {max_message_length} bits.")
    
    message_index = 0
    
    # Iterate over the pixels and hide the message in the LSB of each pixel
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])  # Get the pixel's RGB values
            
            # Modify the least significant bit of each color channel
            for i in range(3):  # For R, G, and B channels
                if message_index < message_length:
                    pixel[i] = pixel[i] & 0xFE | int(binary_message[message_index])  # Modify LSB
                    message_index += 1
            
            pixels[x, y] = tuple(pixel)  # Update the pixel with the new values
    
    # Save the modified image
    image.save(output_path)
    print(f"Message hidden successfully in {output_path}")


def extract_message_from_image(image_path: str, message_length: int) -> str:
    image = Image.open(image_path)
    pixels = image.load()
    
    binary_message = ''
    message_index = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = list(pixels[x, y])
            for i in range(3):  # For each of the color channels
                if message_index < message_length:
                    binary_message += str(pixel[i] & 1)  # Extract the LSB
                    message_index += 1
    
    # Reverse the first function call to get the actual message 
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
    
    return message

def main():
    print("Welcome to my Steganography App!")
    
    input_choice = input("Do you want to (1) Enter a message or (2) Provide a text file? (1/2): ").strip()
    
    if input_choice == '1':
        message = input("Enter the secret message you want to hide within the image: ")
        if not message:
            print("Message cannot be empty!")
            return
    elif input_choice == '2':
        file_path = input("Enter the path to the text file containing the secret message: ")
        try:
            with open(file_path, 'r') as file:
                message = file.read()
            if not message:
                print("The file is empty!")
                return
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return
    else:
        print("Invalid choice! Please enter 1 or 2.")
        return
    
    image_path = input("Enter the path to the image where the message will be hidden: ")
    output_path = input("Enter the path to save the modified image: ")
    hide_message_in_image(image_path, message, output_path)

if __name__ == '__main__':
    main()
