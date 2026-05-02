def solution(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    valid_nums1 = nums1[:m]
    merged = valid_nums1 + nums2
    merged.sort()
    for i in range(m + n):
        nums1[i] = merged[i]
    return nums1


def solution_2(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    i: int = m - 1  # nums 1 counter
    j: int = n - 1  # nums 2 counter
    k: int = m + n - 1  # track pos insert, start from right
    while (
        j >= 0
    ):  # stop condition is to consume nums2, smalelr array that we have to fit all numbers into nums1
        if (
            nums1[i] >= nums2[j] and i >= 0
        ):  # we also need the index cehck, we can never go -1, if we reach this point means we can just fill nums1 with nums2
            to_move: int = nums1[i]
            i -= 1  # we consume, because its a sorted array we know we can move to next number
        else:
            to_move: int = nums2[j]
            j -= 1
        nums1[k] = to_move
        k -= 1  # filled position, we move left
    return nums1


if __name__ == "__main__":
    print(solution_2(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
