import time
import subprocess

init_timer = time.time()

c=0
with open('./rockyou.txt', 'r') as wordlist:
    for line in wordlist:
        entry = line.strip()

        command = ['steghide', 'extract', '-sf', 'fixed_layers.jpg', '-p', entry]

        res = subprocess.run(command, stderr=subprocess.DEVNULL)

        if res.returncode == 0:
            exit(f"[+] Cracked!\n[+] Passphrase: {entry}")

        c += 1

        if c % 50000 == 0:
            execution_time = time.time() - init_timer
            execution_time_formatted = time.strftime("%H:%M:%S", time.gmtime(execution_time))
            print(f"[*] Elapsed time: {execution_time_formatted}")

            print(f"[*] {c} failed attempts. Last passphrase used was {entry}.")
#layers