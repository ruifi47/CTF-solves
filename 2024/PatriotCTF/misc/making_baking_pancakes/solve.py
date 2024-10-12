import base64
import pwn

#pwn.context.log_level = "debug"

r = pwn.remote("chal.pctf.competitivecyber.club", 9001)

for i in range(1000):
    to_parse = r.recvuntil(b" >> ").decode().splitlines()
    challenge = [line for line in to_parse if 'Challenge:' in line][0].split(" ")[-1]
    encoded = base64.b64decode(challenge)
    n = encoded.decode().split("|")[-1]
    to_decode = encoded.decode().split("|")[0]

    for j in range(int(n)):
        to_decode = base64.b64decode(to_decode)

    response = f"{to_decode.decode()}|{i}"
    r.sendline(response.encode())

print(r.recvall().decode())
#pctf{store_bought_pancake_batter_fa82370}
