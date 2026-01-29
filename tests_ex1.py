from ex1 import get_proba

if __name__ == "__main__":
    tests = [
        (
            [(0, 1), (0, 2), (0, 3)],
            0,
            [2, 3],
            2.0 / 3,
        ),
        (
            [(1, 2), (1, 3), (1, 4), (3, 5), (4, 6), (4, 7)],
            1,
            [6, 5],
            0.5,
        ),
    ]

    for labyrinth, start, exits, expected in tests:
        result = get_proba(labyrinth, start, exits)
        diff = abs(result - expected)
        assert diff < 1e-5, (
            f"Wrong probability ! {result} instead of {expected}"
        )

    print("Tests passed !")
