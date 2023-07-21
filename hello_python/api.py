from typing_extensions import TypedDict
from fastapi import FastAPI


class RootRes(TypedDict):
    Hello: str


class ItemRes(TypedDict):
    item_id: int
    q: str | None


app = FastAPI()


@app.get("/")
def read_root() -> RootRes:
    return RootRes(Hello="World!")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> ItemRes:
    return ItemRes(item_id=item_id, q=q)
