def solution(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            is_diag_cell = i == j or (i + j == n - 1)
            if is_diag_cell and matrix[i][j] == 0:
                return False
            elif not is_diag_cell and matrix[i][j] != 0:
                return False
    return True


if __name__ == "__main__":
    print(solution(matrix=[[5, 7, 0], [0, 3, 1], [0, 5, 0]]))
    print(solution(matrix=[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]))
