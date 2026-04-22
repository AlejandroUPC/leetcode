def solution(prices: list[int]) -> list[int]:
    discounted_prices: list[int] = []
    for i in range(len(prices)):
        discount: int = 0
        current_price: int = prices[i]
        for j in range(i + 1, len(prices)):
            compare_price: int = prices[j]
            if compare_price <= current_price:
                discount = compare_price
                break
        discounted_prices.append(current_price - discount)
    return discounted_prices


def solution_2(prices: list[int]) -> list[int]:
    discounted_prices = prices.copy()
    stack: list[int] = []  # indexes waiting to be discounted
    for i in range(len(prices)):
        while stack and prices[i] <= prices[stack[-1]]:
            discounted_prices[stack[-1]] -= prices[i]
            stack.pop()  # we found a discount
        stack.append(i)
    return discounted_prices


if __name__ == "__main__":
    print(solution_2(prices=[8, 4, 6, 2, 3]))
