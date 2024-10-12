import secrets
from base64 import b64encode

def promptGen():
    flipFlops = lambda x: chr(ord(x) + 1)
    with open("topsneaky.txt", "rb") as f:
        first = f.read()
    bittys = secrets.token_bytes(len(first))
    onePointFive = int.from_bytes(first) ^ int.from_bytes(bittys)
    second = onePointFive.to_bytes(len(first))
    third = b64encode(second).decode("utf-8")
    bittysEnc = b64encode(bittys).decode("utf-8")
    fourth = ""
    for each in third:
        fourth += flipFlops(each)
    fifth = f"Mwahahaha you will n{fourth[:10]} ever crack into my pass{fourth[10:]}word, Ill even give you the key and the executable:::: {bittysEnc}"
    return fifth

def main():
    print(promptGen())

if __name__ == "__main__":
    main()
#Mwahahaha you will nOcmu{9gtufever crack into my passMmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ympword, i'll even give you the key and the executable:::: Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV