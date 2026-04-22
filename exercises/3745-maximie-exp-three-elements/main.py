def solution(nums: list[int]) -> int:
    smallest: int = 101
    biggest = [-101]
    for n in nums:
        if n < smallest:
            smallest = n
        if n > min(biggest):
            biggest = [n, max(biggest)]
    return sum(biggest) - smallest


def solution_2(nums: list[int]) -> int:
    min1 = float("inf")
    max1 = max2 = float("-inf")  # max 1 is the largets, max 2 second largest
    for n in nums:
        if n < min1:
            min1 = n
        if n > max1:  # if the biggest number we've
            max2 = max1  # prev biggest is second biggest
            max1 = n  # reassign biggest
        elif n > max2:  # if its only biggest to the second, then
            max2 = n
    return max1 + max2 - min1


if __name__ == "__main__":
    print(solution(nums=[-2, 0, 5, -2, 4]))
