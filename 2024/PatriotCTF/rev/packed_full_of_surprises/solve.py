from Crypto.Cipher import AES

key = 0xefcdab8967452301.to_bytes(8, 'little')
key += 0xfedcba9876543210.to_bytes(8, 'little')
key += 0x8796a5b4c3d2e1f0.to_bytes(8, 'little')
key += 0xf1e2d3c4b5a6978.to_bytes(8, 'little')

iv = 0x706050403020100.to_bytes(8, 'little')
iv += 0xf0e0d0c0b0a0908.to_bytes(8, 'little')

cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
enc = open("flag.txt.enc", "rb").read()
flag = cipher.decrypt(enc)
print(flag.decode())
#PCTF{UPX_15_2_3A$y_t0_uNp4cK}
