init="K0c2QjkVcRd1eyFWcUArUDF7NRQwUCp7ckIdR3JRMFdxVz8="
import base64
step1 = base64.b64decode(init)
c=0
flag=""
for byte in step1:
    if c%2==0:
        flag += chr(byte^66)
    else:
        flag += chr(byte^36)
    c+=1
print(flag)
#ictf{1337_cr3dits_w0rth_0f_c0urs3s}