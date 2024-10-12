import re
import binascii

def split_data(raw_hex_data):
    pattern = re.compile(r'ffd8(.*?)ffd9', re.DOTALL)
    matches = re.findall(pattern, raw_vnc_data)
    image_data_array = [binascii.unhexlify('ffd8' + match + 'ffd9') for match in matches]
    return image_data_array

def save_images(image_data_array):
    for i, image_data in enumerate(image_data_array):
        with open(f'image_{i + 1}.jpeg', 'wb') as file:
            file.write(image_data)

if __name__ == "__main__":
    with open('raw.data', 'r') as file:
        raw_vnc_data = file.read()

    raw_vnc_data = ''.join(raw_vnc_data.split())
    save_images(split_data(raw_vnc_data))
