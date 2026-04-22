from main import solution


def run_tests() -> None:
    assert solution(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert solution(numbers=[2, 3, 4], target=6) == [1, 3]
    assert solution(numbers=[-1, 0], target=-1) == [1, 2]


if __name__ == "__main__":
    run_tests()
