def solution(n: int) -> int:
    board: list[int] = [n]
    memo: set = set()  # this is to not re-compute board, if we computed board once it will be same results
    for day in range(
        0, 10
    ):  # NOTE: for testing purposes, reducing this to 10, range(1, (10**9) + 1): this will break for bigger n's
        if tuple(board) in memo:
            # print("Continue")
            continue
        memo.add(tuple(board))
        to_add = []
        # print(f"Working on {day=}.")
        for number in board:
            # print(f"Working on {number=} of {board=}.")
            for num_check in range(1, n + 1):
                # print(f"Checking {num_check=} vs {number=}.")
                if number % num_check == 1:
                    # print(f"Bing on {number}%{num_check}={number % num_check}.")
                    if num_check not in board:
                        to_add.append(num_check)
        board.extend(to_add)
        # print(f"After {day=} we got {board=}.")
    return len(board)


def solution_2(n: int) -> int:
    if n == 1:
        return n
    return n - 1


if __name__ == "__main__":
    print(solution(n=3))
