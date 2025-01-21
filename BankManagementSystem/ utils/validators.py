def validate_account_number(account_number):
    return len(account_number) == 10 and account_number.isdigit()