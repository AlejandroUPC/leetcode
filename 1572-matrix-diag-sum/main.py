def solution(mat: list[list[int]]) -> int:
    matrix_dim = len(mat)
    left_right_diag = 0
    right_left_diag = matrix_dim - 1
    total = 0
    for row in mat:
        if right_left_diag != left_right_diag:
            total += row[left_right_diag] + row[right_left_diag]
        else:
            total += row[
                left_right_diag
            ]  # we just some once when we meet in the exact center of a matrix (when n = odd)
        left_right_diag += 1
        right_left_diag -= 1
    return total


def solution_2(mat: list[list[int]]) -> int:
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][i]  # primary diagonal

        if i != n - 1 - i:
            total += mat[i][n - i - 1]
    return total


if __name__ == "__main__":
    print(solution(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution([[1] * 4] * 4))
