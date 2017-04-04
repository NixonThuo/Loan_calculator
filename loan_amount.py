def loan(amount, rate, time):
    while True:
        try:
            if time <= 12:
                interest = amount * rate / 100 * time / 12
                total_loan = interest + amount
                return total_loan
        except(AttributeError, ValueError, TypeError):
            return "Invalid"


print loan(10000, 12, 12)