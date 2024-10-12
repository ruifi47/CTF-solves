'''
int64_t print_flag()
{
    int64_t var_48;
    __builtin_memcpy(&var_48, "\xa1\x8f\xd7\xb2\xf2\xfa\x48\x39\x6b\xc2\x92\x10\x58\x44\x65\x8c\x4a\x75\x56\x0b\x66\x51\x68\x89\x8d\x0c\xfd\x8d\x67\x22\xdf\x0f\xca\x8f\x9b\x25\xb9", 0x25);
    int64_t str;
    __builtin_memcpy(&str, "\xaa\x2f\xe5\x58\xb8\x6a\x3c\x33\x15\xd6\x58\x42\x38\x31\x62\xde\xcd\xa4\xe9\xb8\xe8\xbd\xfc\x77\xa2\x89\x7a\xc1\xa2\xda\x33\x37\xd8\x4b\x9d\xb9\x14", 0x25);
    int64_t i_1 = 0x25;
    for (int32_t i = 0x24; i > 0; i = (i - 1))
    {
        *(&str + i) = (*(&str + (i - 1)) ^ *(&str + i));
    }
    int32_t var_10 = 0;
    while (var_10 < i_1)
    {
        *(&str + var_10) = (*(&str + var_10) ^ 0x69);
        var_10 = (var_10 + 1);
    }
    int32_t var_14 = 0;
    while (var_14 < i_1)
    {
        *(&str + var_14) = (*(&var_48 + var_14) ^ *(&str + var_14));
        var_14 = (var_14 + 1);
    }
    return puts(&str);
}
'''

def get_flag():
    var_48 = bytearray(b'\xa1\x8f\xd7\xb2\xf2\xfa\x48\x39\x6b\xc2\x92\x10\x58\x44\x65\x8c\x4a\x75\x56\x0b\x66\x51\x68\x89\x8d\x0c\xfd\x8d\x67\x22\xdf\x0f\xca\x8f\x9b\x25\xb9')
    str_var = bytearray(b'\xaa\x2f\xe5\x58\xb8\x6a\x3c\x33\x15\xd6\x58\x42\x38\x31\x62\xde\xcd\xa4\xe9\xb8\xe8\xbd\xfc\x77\xa2\x89\x7a\xc1\xa2\xda\x33\x37\xd8\x4b\x9d\xb9\x14')

    for i in range(36, 0, -1):
        str_var[i] = str_var[i-1] ^ str_var[i]

    i_1 = 0x25
    var_10 = 0
    while var_10 < i_1:
        str_var[var_10] = str_var[var_10] ^ 0x69
        var_10 += 1

    var_14 = 0
    while var_14 < i_1:
        str_var[var_14] = var_48[var_14] ^ str_var[var_14]
        var_14 += 1

    return str(str_var, 'utf-8')

print(get_flag())
#bctf{Aw_$hucK$_Y0ur3_m@k1Ng_m3_bLu$h}
