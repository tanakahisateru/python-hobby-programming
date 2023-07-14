from game import *


def test_time_to_radius():
    assert time_to_radius(0, 30, 40) == 20
    assert time_to_radius(15, 30, 40) == 20
    assert time_to_radius(30, 30, 40) == 20
