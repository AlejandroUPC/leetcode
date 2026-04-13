def solution(num: int) -> int:
    cter = 0
    while num != 0:  # we assume we will always reach 0, we assume 0.X is also 0
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        cter += 1
        print(f"{num=} on {cter=}.")
    return cter


if __name__ == "__main__":
    print(solution(num=14))
