import pyxel


def add(a, b):
    return a + b


if __name__ == '__main__':
    pyxel.init(120, 120)
    pyxel.cls(1)
    pyxel.circb(60, 60, 40, 7)
    pyxel.show()
