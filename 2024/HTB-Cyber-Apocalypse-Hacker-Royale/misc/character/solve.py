from pwn import *

r=remote('94.237.48.205',40890)

flag='HTB{'
index=4
while flag[-1] != '}':
    r.sendlineafter(b'index: ', str(index).encode())
    flag_letter=r.recvline().decode()[-2:][0]
    flag+=flag_letter
    index+=1

print(flag)
#HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}
