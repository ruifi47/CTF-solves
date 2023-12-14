from pwn import *

'''
  ___________
 /           \
/___|0|0|0|___\
|      @      |
|_____________|
Enter 1 to rotate the lock, or 2 to exit
1
Which wheel would you like to rotate? (1-3)
1
Which direction would you like to rotate the wheel? (+/-)
+
  ___________
 /           \
/___|1|0|0|___\
|      @      |
|_____________|
The chest is still locked!
Enter 1 to rotate the lock, or 2 to exit
'''

context.log_level = 'debug'

r = remote("chal.tuctf.com", 30002)

for a in range(10):
    for b in range(10):
        for c in range(10):
            r.sendlineafter(b"Enter 1 to rotate the lock, or 2 to exit\n", b"1")
            r.sendlineafter(b"Which wheel would you like to rotate? (1-3)\n", b"1")
            r.sendlineafter(b"Which direction would you like to rotate the wheel? (+/-)\n", b"+")
            [r.recvline() for i in range(6)]

        r.sendlineafter(b"Enter 1 to rotate the lock, or 2 to exit\n", b"1")
        r.sendlineafter(b"Which wheel would you like to rotate? (1-3)\n", b"2")
        r.sendlineafter(b"Which direction would you like to rotate the wheel? (+/-)\n", b"+")
        [r.recvline() for i in range(6)]

    r.sendlineafter(b"Enter 1 to rotate the lock, or 2 to exit\n", b"1")
    r.sendlineafter(b"Which wheel would you like to rotate? (1-3)\n", b"3")
    r.sendlineafter(b"Which direction would you like to rotate the wheel? (+/-)\n", b"+")
    [r.recvline() for i in range(6)]
#TUCTF{h3R3_1!3_M3_800Ty}