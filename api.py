from typing import Any
from fastapi import FastAPI
# from typing import Optional

app = FastAPI()

@app.get("/")
def read_root() -> dict[str,Any]:
    return {"Hello": "World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str|None = None) -> dict[str,Any]:
    return {"item_id": item_id, "q": q}
