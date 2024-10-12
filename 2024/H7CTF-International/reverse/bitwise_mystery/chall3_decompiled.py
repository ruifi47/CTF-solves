flag = 'REDACTED'
n = flag
c = int(input('Enter a number: '))
if len(n) % 2:
    n += '*'
m = []
for i in range(0, len(n), 2):
    a, b = (ord(n[i]), ord(n[i + 1]))
    m.append((a << c) + b)
print(m)
