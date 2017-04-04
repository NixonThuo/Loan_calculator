def loan(amount, rate, time):
    if time <= 12 and all(isinstance(i, int) for i in [amount, rate, time]):
        interest = amount * rate / 100 * time / 12
        total_loan = interest + amount
        return total_loan
    else:
        return "Invalid"


print loan(10000, 12, 5)
