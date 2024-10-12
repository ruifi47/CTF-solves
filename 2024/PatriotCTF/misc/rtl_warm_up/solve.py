import re

with open('flag.vcd', 'r') as f:
    content = f.read()

data = re.findall(r'b([01]+) "\n', content)
flag = ''.join(chr(int(b, 2)) for b in data)
print(flag)
#PCTF{RTL_i$_D@D_0F_H@rdw@r3}
