from pwn import *

context.log_level = 'debug'

r = remote("chals.sekai.team", 9000)
[r.recvline() for i in range(4)]

for i in range(100):
    conta = r.recvline()
    resultado = eval(conta)
    r.sendline(str(resultado))
    r.recvline()

last = r.recvall()
print(last)
