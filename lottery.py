from secrets import randbelow


def gen_lottery_number():
    nums = []
    total = 0

    while total <= 5:
        nums.append(randbelow(69))
        total += 1

    return nums


def main():
    money_spent = 0
    rolled_numbers = gen_lottery_number()

    match_thresh = int(input("Thank you for playing the lottery! How many numbers are you trying to match? 1-5\n"))
    price = 3 if int(input("Would you like to buy the powerball?\n 1 for true 2 for false")) == 1 else 2

    print(f"\nYour lottery number is: {rolled_numbers}")
    matches = 0
    ticket_num = ""

    try:
        while matches < match_thresh:
            money_spent += price
            matches = 0

            ticket_num = gen_lottery_number()

            for num in ticket_num:
                matches += 1 if num in rolled_numbers else 0

            ticket_num = "-".join(map(str, ticket_num))
            print(f"\nYour Number was: {ticket_num}, with {matches} matches. You've spent ${money_spent}")

        rolled_numbers = "-".join(map(str, rolled_numbers))

        print(f"""
            You hit a match!
            The lottery Number was: {rolled_numbers}
            Your winning Number   : {ticket_num} and {matches} matches!
            You bought {int(money_spent/price)}, costing ${money_spent} in total.
            You could buy roughly {int(money_spent/1.86)} eggs with that money.\n
            .\n
            .\n
        """)
    except KeyboardInterrupt:
        print(f"""\nThe starting number was:{rolled_numbers}\n
        You bought {money_spent/price} lotto tickets and spent ${money_spent}.
        """)


main()
