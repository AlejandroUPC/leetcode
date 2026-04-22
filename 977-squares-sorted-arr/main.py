def solution(nums: list[int]) -> list[int]:
    return list(sorted(x**2 for x in nums))


def solution_2(nums: list[int]) -> list[int]:
    sorted_squares: list[int] = [0]
    left = 0
    right = len(nums) - 1
    while left <= right:
        left_square: int = nums[left] ** 2
        right_square: int = nums[right] ** 2
        if left_square >= right_square:
            left += 1
            sorted_squares.insert(0, left_square)
        else:
            sorted_squares.insert(0, right_square)
            right -= 1
    return sorted_squares


if __name__ == "__main__":
    print(solution_2(nums=[-7, -3, -1, 2, 4, 9]))
