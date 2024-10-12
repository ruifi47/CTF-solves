encrypted_flag = [62,63,40,58,39,40,111,63,52,50,53,63,104,48,48,37,3,61,3,55,57,37,48,108,59,59,111,46,33]
flag = ''.join([chr(x ^ 92) for x in encrypted_flag])
print(flag)
#bctf{t3chnic4lly_a_keyl0gg3r}
