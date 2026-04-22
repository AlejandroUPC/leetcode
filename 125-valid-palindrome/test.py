from main import solution, solution_2


def run_tests() -> None:
    assert solution(s="A man, a plan, a canal: Panama")
    assert not solution(s="race a car")
    assert solution(s=" ")
    assert solution_2(s="A man, a plan, a canal: Panama")
    assert not solution_2(s="race a car") 
    assert solution_2(s=" ")


if __name__ == "__main__":
    run_tests()
