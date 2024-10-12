from pwn import *

printable = string.printable

not_blacklist=[]
for char in printable:
    conn = remote("dyn.ctf.pearlctf.in", 30016)
    conn.sendlineafter('>>> ', encode(char))
    print(f"testing '{char}'")
    response = conn.recvline()
    if "Your sentence has been increased by 2 years for attempted escape." not in response.decode():
        print(f'{char} is not blacklisted!')
        not_blacklist.append(char)
print(not_blacklist)
#['a', 'c', 'h', 'q', 'r', 'w', '"', "'", '(', ')', '+', '-', '=', '?', '\\', '`', '|', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
