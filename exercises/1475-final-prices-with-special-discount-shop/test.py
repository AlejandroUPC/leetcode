from main import solution, solution_2


def run_tests() -> None:
    assert solution(prices=[8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
    assert solution(prices=[1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert solution(prices=[10, 1, 1, 6]) == [9, 0, 1, 6]
    assert solution_2(prices=[8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
    assert solution_2(prices=[1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert solution_2(prices=[10, 1, 1, 6]) == [9, 0, 1, 6]


if __name__ == "__main__":
    run_tests()
