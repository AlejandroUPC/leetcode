def solution(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area


def solution_2(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        local_area = min(height[left], height[right]) * (right - left)
        if local_area > max_area:
            max_area = local_area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area
if __name__ == "__main__":
    print(solution(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solution_2(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
