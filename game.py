import math
import pyxel


class Game:
    frame: int

    def __init__(self) -> None:
        self.frame = 0

    def update(self) -> None:
        self.frame += 1

    def draw(self) -> None:
        pyxel.cls(1)
        r = time_to_radius(self.frame, 30, 40)
        pyxel.circb(60, 60, r, 7)


def time_to_radius(frame:int, cycle:float, radius:int) -> int:
    t = 2 * math.pi * frame / cycle
    r_half = radius / 2
    return round(r_half * math.sin(t) + r_half)


if __name__ == '__main__':
    pyxel.init(120, 120)
    game = Game()
    pyxel.run(game.update, game.draw)
