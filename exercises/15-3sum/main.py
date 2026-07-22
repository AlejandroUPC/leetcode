def solution(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []

    for i, anchor in enumerate(nums):
        if i > 0 and anchor == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        target = -anchor
        while left < right:
            local_total = nums[left] + nums[right]
            if local_total < target:
                left += 1
            elif local_total > target:
                right -= 1
            else:
                res.append([anchor, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return res


if __name__ == "__main__":
    print(solution([1, 2, 3]))
