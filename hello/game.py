import math
import threading
import urllib.request
import urllib.error
import pyxel


class ZoomAnimationCircle:
    cycle: int = 30
    radius: int

    def __init__(self, cycle: int = 30, radius: int = 40) -> None:
        self.cycle = cycle
        self.radius = radius
        self._frame = 0

    def step(self, progress: int = 1) -> None:
        self._frame += progress

    def current_r(self) -> int:
        t = 2 * math.pi * self._frame / self.cycle
        r_half = self.radius / 2
        return round(r_half * math.sin(t) + r_half)


class Game:
    def __init__(self) -> None:
        self.figure = ZoomAnimationCircle()
        self.worker = PingWorker("http://127.0.0.1:8000/")

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.worker.ping()

        self.figure.step()

    def draw(self) -> None:
        pyxel.cls(1)
        pyxel.circb(60, 60, self.figure.current_r(), 7)


class PingWorker:
    def __init__(self, url: str):
        self.url = url
        self.running_count = 0
        self.lock = threading.Lock()

    def safe_running_count(self):
        with self.lock:
            return self.running_count

    def ping(self):
        with self.lock:
            self.running_count += 1
            thread = threading.Thread(target=self._ping)
            thread.start()

    def _ping(self):
        # print(threading.current_thread().name, "start", self.safe_running_count())

        req = urllib.request.Request(self.url, method="GET")
        try:
            with urllib.request.urlopen(req) as res:
                body = res.read().decode("utf-8")
            print(body)
            # time.sleep(2)
        except urllib.error.URLError as e:
            print(e.reason)
            return
        finally:
            with self.lock:
                self.running_count -= 1
            # print(threading.current_thread().name, "end", self.safe_running_count())


def boot():
    pyxel.init(120, 120)
    game = Game()
    pyxel.run(game.update, game.draw)


if __name__ == "__main__":
    boot()
