from ex3 import solve_level

if __name__ == "__main__":

    def manhattan_dist(p1, p2):
        diff_x = abs(p1[0] - p2[0])
        diff_y = abs(p1[1] - p2[1])
        return diff_x + diff_y <= 1

    def validate_path(lab, path):
        old_pos = None
        for i, pos in enumerate(path):
            if i == 0:
                old_pos = pos
                continue
            if not manhattan_dist(old_pos, pos):
                # Movement not correct !
                return False
            if lab[pos[0]][pos[1]] == "w":
                print("Reason : Stepped on a permanent wall")
                return False
            if lab[pos[0]][pos[1]] == "e" and i % 2 == 0:
                print(f"Reason : Stepped on a even wall at time {i}")
                return False
            if lab[pos[0]][pos[1]] == "o" and i % 2 == 1:
                print(f"Reason : Stepped on a odd wall at time {i}")
                return False
            old_pos = pos
        return True

    # This contains a list of tests where each element is :
    # (Labyrinth, Start cell, Destination cell, Expected length)
    tests = [
        (
            [
                ["", "w", "", "", ""],
                ["", "w", "o", "w", ""],
                ["", "w", "", "w", ""],
                ["", "o", "", "w", ""],
            ],
            (0, 0),
            (3, 4),
            15,
        ),
        (
            [
                ["", "w", "", "", ""],
                ["", "w", "", "w", ""],
                ["", "w", "", "w", ""],
                ["", "", "", "w", ""],
            ],
            (0, 0),
            (3, 4),
            14,
        ),
        (
            [
                ["", "w", "", "", ""],
                ["", "w", "o", "w", ""],
                ["", "w", "", "w", ""],
                ["", "o", "o", "w", ""],
            ],
            (0, 0),
            (3, 4),
            0,
        ),
    ]
    for lab, start, end, expected in tests:
        path = solve_level(lab, start, end)
        assert validate_path(lab, path), "Path is not valid"
        assert len(path) == expected, f"Path length is not {expected}"
    print("All tests passed!")
