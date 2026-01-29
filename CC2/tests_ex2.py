from ex2 import plan_tour

if __name__ == "__main__":
    tests = [
        (
            [
                (0, 1, 20),
                (1, 2, 30),
                (2, 3, 50),
                (2, 0, 10),
                (1, 3, 20),
                (0, 3, 60),
            ],
            0,
            3,
            40,
        ),
        (
            [
                (0, 1, 10),
                (1, 2, 10),
                (2, 3, 10),
                (2, 0, 10),
                (1, 3, 20),
                (0, 3, 60),
            ],
            0,
            3,
            30,
        ),
    ]
    for map, src, dest, expected_length in tests:
        assert plan_tour(map, src, dest) == expected_length, (
            "A test has failed !"
        )
    print("Tests successful !")
