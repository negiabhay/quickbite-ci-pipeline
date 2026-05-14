from app import calculate_total, apply_discount

def test_calculate_total():
    result = calculate_total(200, 3)
    assert result == 600

def test_apply_discount():
    result = apply_discount(600, 10)
    assert result == 540.0
