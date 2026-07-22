from main import solution


def run_tests() -> None:
    assert solution([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert solution([0, 1, 1]) == []
    assert solution([0, 0, 0]) == [[0, 0, 0]]
    assert solution([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]


if __name__ == "__main__":
    run_tests()
