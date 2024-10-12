'''
$ nc 83.136.252.194 57910
===== THE FRAY: THE VIDEO GAME =====
Welcome!
This video game is very simple
You are a competitor in The Fray, running the GAUNTLET
I will give you one of three scenarios: GORGE, PHREAK or FIRE
You have to tell me if I need to STOP, DROP or ROLL
If I tell you there's a GORGE, you send back STOP
If I tell you there's a PHREAK, you send back DROP
If I tell you there's a FIRE, you send back ROLL
Sometimes, I will send back more than one! Like this: 
GORGE, FIRE, PHREAK
In this case, you need to send back STOP-ROLL-DROP!
Are you ready? (y/n) y
Ok then! Let's go!
FIRE, FIRE, GORGE, GORGE, GORGE
What do you do? ROLL, ROLL, STOP, STOP, STOP
Unfortunate! You died!
'''

from pwn import *

#context.log_level='debug'

r=remote('83.136.252.194', 57910)

res = {
    'GORGE': 'STOP',
    'PHREAK': 'DROP',
    'FIRE': 'ROLL',
}

r.sendlineafter(b'Are you ready? (y/n) ', b'y')
r.recvline()
for i in range(1337):
    input = r.recvline().decode().strip().split(', ')
    print(input)
    reply = '-'.join([res[i] for i in input])
    print(reply)
    r.sendlineafter(b'What do you do? ', reply.encode())
#HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}