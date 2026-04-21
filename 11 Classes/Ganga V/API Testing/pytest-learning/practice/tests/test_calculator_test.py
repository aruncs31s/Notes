# Calculator Tests - Practice File

from calculator import add, subtract, multiply, divide, get_user


class TestCalculator:
    
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2
    
    def test_add_zero(self):
        assert add(0, 0) == 0
    
    def test_subtract(self):
        assert subtract(10, 5) == 5
    
    def test_multiply(self):
        assert multiply(3, 4) == 12
    
    def test_divide(self):
        assert divide(10, 2) == 5
    
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)


class TestGetUser:
    
    def test_get_existing_user(self):
        user = get_user(1)
        assert user is not None
        assert user["name"] == "Alice"
    
    def test_get_nonexistent_user(self):
        user = get_user(999)
        assert user is None
