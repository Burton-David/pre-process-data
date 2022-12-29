import base64


class DataEncoder:
    def __init__(self):
        pass

    def base64_encode(self, data: bytes) -> str:
        """Encode data using base64 encoding.

        Args:
        - data: The data to be encoded, as a bytes object.

        Returns:
        - The base64-encoded data, as a string.
        """
        return base64.b64encode(data).decode('utf-8')

    def base64_decode(self, data: str) -> bytes:
        """Decode data that has been encoded using base64 encoding.

        Args:
        - data: The data to be decoded, as a string.

        Returns:
        - The decoded data, as a bytes object.
        """
        return base64.b64decode(data)

    def rot13_encode(self, data: str) -> str:
        """Encode data using ROT13 encoding.

        Args:
        - data: The data to be encoded, as a string.

        Returns:
        - The ROT13-encoded data, as a string.
        """
        encoded_data = ''
        for char in data:
            if char.isalpha():
                if char.isupper():
                    char = chr((ord(char) - 65 + 13) % 26 + 65)
                else:
                    char = chr((ord(char) - 97 + 13) % 26 + 97)
            encoded_data += char
        return encoded_data

    def rot13_decode(self, data: str) -> str:
        """Decode data that has been encoded using ROT13 encoding.

        Args:
        - data: The data to be decoded, as a string.

        Returns:
        - The decoded data, as a string.
        """
        return self.rot13_encode(data)

    def xor_encode(self, data: bytes, key: bytes) -> bytes:
        """Encode data using XOR encryption.

        Args:
        - data: The data to be encoded, as a bytes object.
        - key: The key to use for the XOR encryption, as a bytes object.

        Returns:
        - The XOR-encrypted data, as a bytes object.
        """
        encoded_data = bytearray(len(data))
        for i in range(len(data)):
            encoded_data[i] = data[i] ^ key[i % len(key)]
        return bytes(encoded_data)

    def xor_decode(self, data: bytes, key: bytes) -> bytes:
        """Decode data that has been encoded using XOR encryption.

        Args:
        - data: The data to be decoded, as a bytes object.
        - key: The key that was used for the XOR encryption, as a bytes object.

        Returns:
        - The decrypted data, as a bytes object.
        """
        return self.xor_encode(data, key)
