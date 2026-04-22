from main import solution, solution_2


def run_tests() -> None:
    assert solution(n=3) == 2
    assert solution(n=5) == 4
    assert solution_2(n=3) == 2
    assert solution_2(n=5) == 4


if __name__ == "__main__":
    run_tests()
