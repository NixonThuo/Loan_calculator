def loan(amount, rate, time):
    if time <= 12:
        interest = amount * rate / 100 * time / 12
        total_loan = interest + amount
        return total_loan
    else:
        return "Invalid"


print loan(10000, 12, 14)
