import dis
import marshal

with open('passwordProtector.pyc', 'rb') as f:
    f.seek(16)
    code = marshal.load(f)
    dis.dis(code)
