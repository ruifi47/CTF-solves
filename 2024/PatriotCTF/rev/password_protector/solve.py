from base64 import b64decode

flipFlops = lambda x: chr(ord(x) - 1)
bittysEnc = "Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV"
fourth = "Ocmu{9gtufMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp"
third = "".join(map(flipFlops, fourth))
second = b64decode(third + "=" * (-len(third) % 4))
onePointFive = int.from_bytes(second) ^ int.from_bytes(b64decode(bittysEnc))
first = onePointFive.to_bytes((onePointFive.bit_length() + 7) // 8)
print(first.decode())
#PCTF{I_<3_$3CUR1TY_THR0UGH_0B5CUR1TY!!}