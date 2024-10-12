enc = open('trap', 'rb').read()

# sha1 key -> '6aef677b2c8b645384e713aece4322b045a79f48'
key = b'whatthehelldoyouthinkyouaredoing'  # plaintext key

from pwn import xor

dec = xor(enc, key)

print(dec.decode())
#H7CTF{wh@_1N_7h3!r_r1gh7_m1nd_r@v3r$es_j@v4$scr!pt_L0LL!}
