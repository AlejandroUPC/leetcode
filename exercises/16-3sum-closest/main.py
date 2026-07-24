import math


def solution(nums: list[int], target: int) -> int:
    nums.sort()
    min_dist = math.inf
    res = 0
    for i in range(0, len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[i] + nums[right]
            current_dist = abs(target - current_sum)
            if current_dist < min_dist:
                min_dist = current_dist
                res = current_sum
            if current_sum == target:
                return current_sum
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
    return res


if __name__ == "__main__":
    print(solution(nums=[-1, 2, 1, -4], target=1))
    print(solution(nums=[0, 0, 0], target=1))
    print(solution(nums=[1, 1, 1, 1], target=0))
    print(solution(nums=[10, 20, 30, 40, 50, 60, 70, 80, 90], target=1))
