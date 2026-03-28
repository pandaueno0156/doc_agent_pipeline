#src/validators/amount.py

def validate_amount(amount) ->bool:
    try:
        amount = int(amount)
        return amount % 10 == 0
    except (ValueError, TypeError):
        return False