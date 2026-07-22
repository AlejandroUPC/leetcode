from main import solution, solution_2


def run_tests() -> None:
    assert solution([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution([1, 1]) == 1
    assert solution([1, 2, 1]) == 2
    assert solution_2([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution_2([1, 1]) == 1
    assert solution_2([1, 2, 1]) == 2


if __name__ == "__main__":
    run_tests()
