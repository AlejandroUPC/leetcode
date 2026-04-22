from main import solution, solution_2


def run_tests() -> None:
    assert solution([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert solution([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert solution_2([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert solution_2([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]


if __name__ == "__main__":
    run_tests()
