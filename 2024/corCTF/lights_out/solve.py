import random
import time
import sys
import os
from pwn import remote


def generate_random_board(n: int) -> list[int]:
    board = [random.randint(0, 1) for _ in range(n * n)]
    return board


def create_vector_representations(n: int) -> list[list[int]]:
    vectors = []
    for i in range(n * n):
        vector = [0] * (n * n)
        vector[i] = 1
        if i % n != 0:
            vector[i - 1] = 1  # left
        if i % n != n - 1:
            vector[i + 1] = 1  # right
        if i >= n:
            vector[i - n] = 1  # up
        if i < n * (n - 1):
            vector[i + n] = 1  # down
        vectors.append(vector)
    return vectors


def create_augmented_matrix(vectors: list[list[int]], board: list[int]) -> list[list[int]]:
    matrix = [vec + [board[i]] for i, vec in enumerate(vectors)]
    return matrix


def print_board(board: list[int], n: int) -> str:
    board_string = ""
    for i in range(n):
        row = ""
        for j in range(n):
            row += "#" if board[i * n + j] else "."
        board_string += row + "\n"
    return board_string


def gauss_jordan_elimination(matrix: list[list[int]]) -> list[list[int]]:
    rows, cols = len(matrix), len(matrix[0])
    r = 0
    for c in range(cols - 1):
        if r >= rows:
            break
        pivot = None
        for i in range(r, rows):
            if matrix[i][c] == 1:
                pivot = i
                break
        if pivot is None:
            continue
        if r != pivot:
            matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        for i in range(rows):
            if i != r and matrix[i][c] == 1:
                for j in range(cols):
                    matrix[i][j] ^= matrix[r][j]
        r += 1
    return matrix


def is_solvable(matrix: list[list[int]]) -> bool:
    rref = gauss_jordan_elimination(matrix)
    for row in rref:
        if row[-1] == 1 and all(val == 0 for val in row[:-1]):
            return False
    return True


def get_solution(board: list[int], n: int) -> list[int] | None:
    vectors = create_vector_representations(n)
    matrix = create_augmented_matrix(vectors, board)
    if not is_solvable(matrix):
        return None
    rref_matrix = gauss_jordan_elimination(matrix)
    return [row[-1] for row in rref_matrix[:n * n]]


def check_solution(board: list[int], solution: list[int], n: int) -> bool:
    for i in range(n * n):
        if solution[i] == 1:
            board[i] ^= 1
            if i % n != 0:
                board[i - 1] ^= 1  # left
            if i % n != n - 1:
                board[i + 1] ^= 1  # right
            if i >= n:
                board[i - n] ^= 1  # up
            if i < n * (n - 1):
                board[i + n] ^= 1  # down
    return all(val == 0 for val in board)


def main():
    conn = remote('be.ax', 32421)

    data = conn.recvuntil(b'Your Solution: ').decode()
    board_str = data.split('Lights Out Board:')[1].split('Your Solution:')[0].strip()
    board_lines = board_str.split('\n')
    n = len(board_lines)
    board = [1 if c == '#' else 0 for line in board_lines for c in line]

    solution = get_solution(board, n)
    if solution is None:
        print("No solution found.")
        return

    solution_str = ''.join(['#' if x == 1 else '.' for x in solution])
    conn.sendline(solution_str)
    response = conn.recvall().decode()
    print(response)


if __name__ == "__main__":
    main()
#corctf{freshman_math_class_throwback}
