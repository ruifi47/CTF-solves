def reverse_transformation(output):
    part_len = (len(output) + 2) // 3

    part1 = output[:part_len]
    part2 = output[part_len:2 * part_len]
    part3 = output[2 * part_len:]

    input = []

    for i in range(part_len):
        if i < len(part1):
            input.append(part1[i])
        if i < len(part2):
            input.append(part2[i])
        if i < len(part3):
            input.append(part3[i])

    return ''.join(input)

out = "HT859092947c87F4cff7727181C{872a2ba640}"
print(reverse_transformation(out))
#H7CTF{8485c79f20fa97227b92a476714c8081}
