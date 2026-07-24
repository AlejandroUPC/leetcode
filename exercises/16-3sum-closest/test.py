from main import solution


def run_tests() -> None:
    assert solution(nums=[-1, 2, 1, -4], target=1) == 2
    assert solution(nums=[0, 0, 0], target=1) == 0
    assert solution(nums=[1, 1, 1, 1], target=0) == 3
    assert solution(nums=[10, 20, 30, 40, 50, 60, 70, 80, 90], target=1) == 60


if __name__ == "__main__":
    run_tests()
