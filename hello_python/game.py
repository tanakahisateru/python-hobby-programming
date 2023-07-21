import math
import pyxel


class ZoomAnimationCircle:
    cycle: int
    radius: int

    def __init__(self, cycle: int = 30, radius: int = 40) -> None:
        self.cycle = cycle
        self.radius = radius
        self.frame = 0

    def step(self, progress: int = 1) -> None:
        self.frame += progress

    def current_radius(self) -> int:
        t = 2 * math.pi * self.frame / self.cycle
        r_half = self.radius / 2
        return round(r_half * math.sin(t) + r_half)


class Game:

    def __init__(self) -> None:
        self.figure = ZoomAnimationCircle()

    def update(self) -> None:
        self.figure.step()

    def draw(self) -> None:
        pyxel.cls(1)
        pyxel.circb(60, 60, self.figure.current_radius(), 7)


if __name__ == '__main__':
    pyxel.init(120, 120)
    game = Game()
    pyxel.run(game.update, game.draw)
