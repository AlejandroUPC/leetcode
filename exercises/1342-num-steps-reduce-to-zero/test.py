from main import solution


def run_tests() -> None:
    assert solution(14) == 6
    assert solution(8) == 4
    assert solution(123) == 12


if __name__ == "__main__":
    run_tests()
