from app.core.taxes import calculate_tax_logic

def test_tax_high_value():
    value = 2000.0
    expected_tax = 200.0
    assert calculate_tax_logic(value) == expected_tax

def test_tax_low_value():
    value = 500.0
    expected_tax = 25.0
    assert calculate_tax_logic(value) == expected_tax