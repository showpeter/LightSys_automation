from src.classes import fix_temp as fix

def test_fix():
    test_class = fix.fixture_template("test")
    assert test_class.name == "test"
    test_class2 = fix.fixture_template("test")
    assert test_class2.name != "test"

if __name__ == '__main__':
    test_fix()