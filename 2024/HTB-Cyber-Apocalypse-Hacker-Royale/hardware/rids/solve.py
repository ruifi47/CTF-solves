import socket
import json

def exchange(hex_list, value=0):

    # Configure according to your setup
    host = '83.136.254.167'  # The server's hostname or IP address
    port = 51024          # The port used by the server
    cs=0 # /CS on A*BUS3 (range: A*BUS3 to A*BUS7)

    usb_device_url = 'ftdi://ftdi:2232h/1'

    # Convert hex list to strings and prepare the command data
    command_data = {
        "tool": "pyftdi",
        "cs_pin":  cs,
        "url":  usb_device_url,
        "data_out": [hex(x) for x in hex_list],  # Convert hex numbers to hex strings
        "readlen": value
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Serialize data to JSON and send
        s.sendall(json.dumps(command_data).encode('utf-8'))

        # Receive and process response
        data = b''
        while True:
            data += s.recv(1024)
            if data.endswith(b']'):
                break

        response = json.loads(data.decode('utf-8'))
        #print(f"Received: {response}")
    return response

flag = exchange([0x03], 49)

print(''.join(chr(c) for c in flag))
#HTB{m3m02135_57023_53c2375_f02_3v32y0n3_70_533!@}
