from secrets import randbelow
import atexit


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

    match_thresh = int(input("Thank you for playing the lottery! How many numbers are you trying to match?\n"))

    print(f"\nYour lottery number is: {rolled_numbers}")
    matches = 0
    ticket_num = ""

    try:
        while matches < match_thresh:
            money_spent += 2
            matches = 0

            ticket_num = gen_lottery_number()
            zip_nums = zip(rolled_numbers, ticket_num)

            for num in zip_nums:
                matches += 1 if len(set(num)) == 1 else 0

            ticket_num = "-".join(map(str, ticket_num))
            print(f"\nYour Number was: {ticket_num}, with {matches} matches. You've spent ${money_spent}")

        print(f"""
            You hit a match!
            The lottery Number was: {rolled_numbers}
            You won with: {ticket_num} and {matches} matches!
            You bought {int(money_spent/2)}, costing ${money_spent} in total.
            You could buy roughly {int(money_spent/1.86)} eggs with that money.\n
            .\n
            .\n
        """)
    except KeyboardInterrupt:
        print(f"""\nThe starting number was:{rolled_numbers}\n
        You bought {money_spent/2} lotto tickets and spent ${money_spent}.
        """)


main()
