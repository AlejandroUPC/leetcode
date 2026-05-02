from main import solution, solution_2


def run_tests() -> None:
    solution(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [1, 2, 2, 3, 5, 6]
    solution_2(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [
        1,
        2,
        2,
        3,
        5,
        6,
    ]
    solution(nums1=[1], m=1, nums2=[], n=0) == [1]
    solution_2(nums1=[1], m=1, nums2=[], n=0) == [1]
    solution(nums1=[0], m=0, nums2=[1], n=1) == [1]
    solution_2(nums1=[0], m=0, nums2=[1], n=1) == [1]


if __name__ == "__main__":
    run_tests()
