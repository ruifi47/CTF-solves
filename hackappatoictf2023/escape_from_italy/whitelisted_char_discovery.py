from pwn import *

'''
% nc 92.246.89.201 8889
Just a check you solved last part...
What was the key...?
guera
Oh Oh you escaped from a pasta jail..., can you escape from a bank and steal a precious ruby?...


Welcome to:
HACKAPPATOI's Jewelry (We got funds from zio Berlusca)
Here you will find a magnific 1337 Jewel
 
        _______
      .'_/_|_\_'.
      \`\  |  /`/
       `\\ | //'
         `\|/`
           `

But you need to obtain it and it won't be so easy...
You have a command to get it....
Good Luck!
Enter command:
b
Oopsie.. your input is bad... We blocked it.

'''

import string

allowed_chars = []

for char in string.printable:
    r = remote("92.246.89.201", 8889)
    r.sendlineafter(b"What was the key...?\n", b"guera")
    r.sendlineafter(b"Enter command:\n", char)
    if b"Oopsie.. your input is bad... We blocked it." not in r.recvline():
        log.success(f"char {char} is not blocked!")
        allowed_chars.append(char)

log.info(allowed_chars)
#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'e', 'l', 'v', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~', '\t', '\n', '\r', '\x0b', '\x0c']
