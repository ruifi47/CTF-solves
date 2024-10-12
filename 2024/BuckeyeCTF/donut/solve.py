from pwn import *

context.log_level = 'debug'

conn = remote('challs.pwnoh.io', 13434)

# Receive the initial tower state
initial_data = conn.recvuntil("Enter the stack number you would like to move a donut from (1, 2 or 3):\n").decode()

# Dynamically count the number of donuts on peg 1 by parsing the tower display
lines = initial_data.splitlines()
num_donuts = sum(1 for line in lines if '|' in line and '-' in line)

print(f"Number of donuts: {num_donuts}")

# Define a series of moves based on the Tower of Hanoi algorithm for the number of donuts
# Moves need to go from peg 1 (source) to peg 3 (destination) using peg 2 (auxiliary)
moves = []

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        moves.append((source, target))
    else:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        moves.append((source, target))
        tower_of_hanoi(n - 1, auxiliary, target, source)

# Populate the moves list with the required moves for `num_donuts`
tower_of_hanoi(num_donuts, 1, 3, 2)

# Iterate through the generated moves and interact with the service
for move in moves:
    from_peg, to_peg = move
    conn.sendline(str(from_peg))
    conn.sendlineafter("Enter the stack number you would like to move this donut to (1, 2 or 3):\n", str(to_peg))

    response = conn.recvuntil("Enter the stack number you would like to move a donut from (1, 2 or 3):", drop=False).decode()

    if 'bctf{' in response:
        print("Flag found!")
        conn.interactive()
        break

conn.close()
#bctf{tHe_T0wErs_NeVER_Lie}
