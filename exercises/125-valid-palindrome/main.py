def solution(s: str) -> bool:
    return "".join(c for c in s[::-1].lower() if c.isalnum()) == "".join(
        c for c in s.lower() if c.isalnum()
    )


def solution_2(s: str) -> bool:
    left: int = 0
    right: int = len(s) - 1
    while left < right:
        if s[left] == " " or not s[left].isalnum():
            left += 1
            continue
        if s[right] == " " or not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(solution_2(s="A man, a plan, a canal: Panama"))
