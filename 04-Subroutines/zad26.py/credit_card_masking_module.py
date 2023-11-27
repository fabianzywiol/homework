def mask_credit_card(card_number):
    if len(card_number) == 16:
        masked_number = card_number[:2] + '*' * 10 + card_number[12:]
        return masked_number
    else:
        return "Invalid credit card number"

masked_result = mask_credit_card("5290312400019022")
print(masked_result)
