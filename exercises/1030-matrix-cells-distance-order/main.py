def solution(rows: int, cols: int, r_center: int, c_center: int) -> list[list[int]]:
    distances: list[list[int]] = []
    for r in range(rows):
        for c in range(cols):
            distance = (abs(r - r_center), abs(c - c_center))
            distances.append(list(distance))
    return list(
        sorted(distances, key=lambda x: abs(x[0] - r_center) + abs(x[1] - c_center))
    )


if __name__ == "__main__":
    # print(solution(rows=1, cols=2, r_center=0, c_center=0))
    print(solution(rows=2, cols=2, r_center=0, c_center=1))
