from main import solution, solution_2


def run_tests() -> None:
    assert solution(nums=[1, 4, 2, 5]) == 8
    assert solution(nums=[-2, 0, 5, -2, 4]) == 11
    assert solution_2(nums=[1, 4, 2, 5]) == 8
    assert solution_2(nums=[-2, 0, 5, -2, 4]) == 11


if __name__ == "__main__":
    run_tests()
