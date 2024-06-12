import bank

def test_starts_with_hello():
    assert bank.value("hello, world") == 0
    assert bank.value("Hello there!") == 0
    assert bank.value("hello123") == 0

def test_starts_with_h():
    assert bank.value("hi, there") == 20
    assert bank.value("how are you?") == 20
    assert bank.value("H123") == 20

def test_other_cases():
    assert bank.value("apple") == 100
    assert bank.value("Good morning") == 100
    assert bank.value("12345") == 100

if __name__ == "__main__":
    test_starts_with_hello()
    test_starts_with_h()
    test_other_cases()
    print("!: PASS :!")