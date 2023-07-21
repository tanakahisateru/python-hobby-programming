from hello_python import game


def test_time_to_radius() -> None:
    fig = game.ZoomAnimationCircle(cycle=60, radius=40)
    assert fig.current_radius() == 20
    fig.step(15)
    assert fig.current_radius() == 40
    fig.step(15)
    assert fig.current_radius() == 20
    fig.step(15)
    assert fig.current_radius() == 0
    fig.step(15)
    assert fig.current_radius() == 20
