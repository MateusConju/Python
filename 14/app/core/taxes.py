def calculate_tax_logic(total_ammount:float) -> float:
    if total_ammount > 1000:
        return total_ammount * 0.10
    return total_ammount * 0.05
