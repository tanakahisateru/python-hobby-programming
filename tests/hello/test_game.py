from hello import game


def test_circle_step() -> None:
    fig = game.ZoomAnimationCircle(cycle=60, radius=40)
    assert fig.current_r() == 20
    fig.step(15)
    assert fig.current_r() == 40
    fig.step(15)
    assert fig.current_r() == 20
    fig.step(15)
    assert fig.current_r() == 0
    fig.step(15)
    assert fig.current_r() == 20
