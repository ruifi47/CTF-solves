def next():
    x = 2
    while True:
        yield x
        x = (15*x + 1) % 143731314793242134

encflag = b'k|\xa6)\xd9\x0c>\x9cq\x8fMf\xd7`\xd4\xdb\x1c\xf2\x84\xb3/<\xdf5\xb8"Q'
sequence = next()

flag = ''
for i, j in zip(sequence, encflag):
    key = round(i) % 256
    flag += chr(j ^ key)

print(flag)
#ictf{sL33P_i5_f0r_tH3_Sl0W}