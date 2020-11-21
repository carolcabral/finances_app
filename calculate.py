from flask_sqlalchemy import SQLAlchemy


def calculate_balance(expenses):
    balance = 0
    print("Calculate_balance:" )
    print(expenses)
    if expenses != []:
        for item in expenses:
            balance += item.value

        return balance/len(expenses)
    else:
        print("Not valid")