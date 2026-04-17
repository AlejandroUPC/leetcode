from collections import Counter


def solution(ransom_note: str, magazine: str) -> bool:
    character_count = Counter(magazine)
    for character in ransom_note:
        is_available = character_count.get(character, 0)
        if not is_available:
            return False
        character_count[character] -= 1
    return True


def solution_2(ransom_note: str, magazine: str) -> bool:
    character_count = [0] * 26
    for character in magazine:
        character_count[ord(character) - ord("a")] += 1

    for character_r in ransom_note:
        idx = ord(character_r) - ord("a")
        if character_count[idx] == 0:
            return False
        else:
            character_count[idx] -= 1
    return True


if __name__ == "__main__":
    print(solution(ransom_note="hello", magazine="helo"))
