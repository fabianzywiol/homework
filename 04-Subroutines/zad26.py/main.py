import credit_card_masking_module

def main():
    credit_card_number = "5290312400019022"
    masked_result = credit_card_masking_module.mask_credit_card(credit_card_number)
    print(f"The masked credit card number: {masked_result}")

if __name__ == "__main__":
    main()
