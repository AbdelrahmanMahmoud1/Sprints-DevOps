from main import *



print(MyFunc([1, 2, 3]))

def test_sum():
    assert MyFunc([1, 2, 3]) == (0, 2), "Should be (0,2)"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")