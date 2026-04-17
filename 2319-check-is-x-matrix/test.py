from main import solution


def run_tests() -> None:
    assert (
        solution(matrix=[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]])
        is True
    )
    assert solution(matrix=[[5, 7, 0], [0, 3, 1], [0, 5, 0]]) is False


if __name__ == "__main__":
    run_tests()
