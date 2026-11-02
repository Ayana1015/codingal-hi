
def total_bill(bill_amount, tip_perc):
    # Calculate final bill after adding tip
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")
    return total