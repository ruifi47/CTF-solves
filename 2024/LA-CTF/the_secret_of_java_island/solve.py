import hashlib

def find_magic_string():
    target_hash = [69, 70, 175, 139, 246, 109, 15, 29, 19, 113, 61, 133, 217, 82, 245, 222, 104, 158, 145, 9, 43, 35, 237, 22, 52, 201, 132, 211, 184, 233, 96, 179]
    for i in range(1 << 8):  # 2^8 combinations
        candidate = ''.join(['p' if i & (1 << j) == 0 else 'd' for j in range(8)])
        if list(hashlib.sha256(candidate.encode()).digest()) == target_hash:
            return candidate
    return None

print(find_magic_string())
#dpddpdpp
#lactf{the_graphics_got_a_lot_worse_from_what_i_remembered}
