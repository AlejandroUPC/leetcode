from main import solution, solution_2


def run_tests() -> None:
    assert solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
    assert solution([[1] * 4] * 4) == 8
    assert solution([[5]]) == 5
    assert solution_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
    assert solution_2([[1] * 4] * 4) == 8
    assert solution_2([[5]]) == 5


if __name__ == "__main__":
    run_tests()
