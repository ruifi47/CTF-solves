ct = 'e18ea0e18e9ae18eabe18e9de18eb2e18e9ae18daae18ea9e18daee18da8e18e9de18da8e18daae18e9be18e96e18da8e18daae18daae18daee18e96e18e9fe18dabe18eafe18da7e18ea9e18d98e18eb4'
ct = bytes.fromhex(ct).decode()
ct = list(ct)
flag = []
for c in ct:
    flag.append(chr(ord(c)-0x1337))

print(''.join(flag))
#ictf{c3r71f13d_1337_h4x0r!}
