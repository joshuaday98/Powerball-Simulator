from secrets import randbelow


def winnings(rolled_numbers, ticket_num,matches,pb,money_spent):
    rewards_dict = {
        "True": {
            1: 4,
            2: 7,
            3: 100,
            4: 50000,
            5: 124000000
        },
        "False": {
            1: 4,
            2: 4,
            3: 7,
            4: 100,
            5: 1000000
        }
    }

    pb_result = str(rolled_numbers[-1] == ticket_num[-1])
    earnings = rewards_dict[pb_result][matches]

    if pb == 3:
        pb_result_text = f"""
            You {'won' if pb_result else 'did not win'} the Powerball.
            Drawing Powerball: {rolled_numbers[-1]}
            Your Powerball: {ticket_num[-1]}
        """
    else:
        pb_result_text = ".\n"

    return f"""
    You hit a match!
    The lottery Number was: {rolled_numbers}
    Your winning Number   : {ticket_num} and {matches} matches!
    You bought {int(money_spent/pb)} tickets.
    You could buy roughly {int(money_spent/1.86)} eggs with that money.\n
    .\n
    {pb_result_text}
    .\n
    Money Stats:
    Spent: {money_spent}
    Winnings: {earnings}
    Profit: {(money_spent * -1) + earnings}
    """

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
    pb = 3 if int(input("Would you like to buy the powerball?\n 1 for true 2 for false")) == 1 else 2

    print(f"\nYour lottery number is: {rolled_numbers}")
    matches = 0
    ticket_num = ""

    try:
        while matches < match_thresh:
            money_spent += pb
            matches = 0

            ticket_num = gen_lottery_number()

            for num in ticket_num:
                if ticket_num.index(num) != len(ticket_num) - 1:
                    try:
                        if num in rolled_numbers and rolled_numbers.index(num) != len(rolled_numbers) -1:
                            matches += 1
                    except:
                        continue

            ticket_num = "-".join(map(str, ticket_num))
            print(f"\nYour Number was: {ticket_num}, with {matches} matches. You've spent ${money_spent}")

        rolled_numbers = "-".join(map(str, rolled_numbers))

        print(winnings(rolled_numbers, ticket_num,matches,pb,money_spent))

    except KeyboardInterrupt:
        print(f"""\nThe starting number was:{rolled_numbers}\n
        You bought {money_spent/pb} lotto tickets and spent ${money_spent}.
        """)


main()
