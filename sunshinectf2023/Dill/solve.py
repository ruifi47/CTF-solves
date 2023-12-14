prefix = 'sun{'
suffix = '}'
o = [5, 1, 3, 4, 7, 2, 6, 0]
encrypted = 'bGVnbGxpaGVwaWNrdD8Ka2V0ZXRpZGls'

def reverse(value: str) -> str:
    value = value[len(prefix):-len(suffix)]
    c = [value[i:i + 4] for i in range(0, len(value), 4)]
    o_inverse = [o.index(i) for i in range(len(o))]
    value = ''.join([c[o_inverse[i]] for i in range(len(c))])
    return value

flag_content = reverse('sun{' + encrypted + '}')

def validate(value: str) -> bool:
    if not (value.startswith(prefix) and value.endswith(suffix)):
        return False
    value = value[len(prefix):-len(suffix)]
    if len(value) != 32:
        return False
    c = [value[i:i + 4] for i in range(0, len(value), 4)]
    value = ''.join([c[i] for i in o])
    if value != encrypted:
        return False
    else:
        print('sun{' + flag_content + '}')

validate('sun{' + flag_content + '}')
#sun{ZGlsbGxpa2V0aGVwaWNrbGVnZXRpdD8K}
