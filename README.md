# hello python

This is my hobby project which can run with even poor Chromebook PC.

Python >= 3.11, SDL2 and Poetry are required.

To start FastAPI server.

```sh
poetry install
poetry run uvicorn hello.api:app
```

Then open another shell.

```sh
poetry run python main.py
```

Click **Boot** button in Tk window to start Pyxel game.

Or start the game directry.

```sh
poetry run pyxel hello/game.py
```

Hit SPACE to send an HTTP message to FastAPI server.
