import app
import main


def test_main_1():
    assert main.A.x == 1

def test_main_2():
    assert app.B.y == 2