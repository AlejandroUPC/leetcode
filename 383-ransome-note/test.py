from main import solution, solution_2


def run_tests() -> None:
    assert solution(ransom_note="a", magazine="b") is False
    assert solution(ransom_note="aa", magazine="ab") is False
    assert solution(ransom_note="aa", magazine="aab") is True

    assert solution_2(ransom_note="a", magazine="b") is False
    assert solution_2(ransom_note="aa", magazine="ab") is False
    assert solution_2(ransom_note="aa", magazine="aab") is True


if __name__ == "__main__":
    run_tests()
