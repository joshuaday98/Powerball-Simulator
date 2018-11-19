from secrets import randbelow


def stringify_ticket_num(num):
    return "-".join(map(str, num))

def gen_ticket_num():
    nums = [[]]
    total = 0

    while total <= 5:
        nums[0].append(randbelow(69))
        total += 1

    nums.append(randbelow(29))

    return nums


class Lotto():
    def __init__(self, match_threshold, powerball):
        self.match_threshold = match_threshold
        self.matches = 0

        self.cost = powerball
        self.pb_bool = True if powerball == 2 else False

        self.drawn_num = gen_ticket_num()
        self.money_spent = 0


    def compare_nums(self, ticket_num):
        #compare ticket numbers
        self.matches = 0
        results = []

        for num in ticket_num[0]:
            if num in self.drawn_num[0]:
                self.matches += 1

        results.append(True if self.matches >= self.match_threshold else False)

        self.money_spent += self.cost

        #check powerball results
        if self.pb_bool:
            results.append(True if self.drawn_num[1] == ticket_num[1] else False)
        else:
            results.append(True)

        return results

    def winnings(self, ticket_num, pb_result):
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

        pb_result_text = ".\n"

        str_drawn_num = stringify_ticket_num(self.drawn_num[0])
        str_ticket_num = stringify_ticket_num(ticket_num[0])

        earnings = rewards_dict[str(self.pb_bool)][self.matches]
        profit = (self.money_spent * -1) + earnings

        print(self.pb_bool)
        if self.pb_bool:
            pb_result_text = f"""
                You won the Powerball!
                Drawing Powerball: {self.drawn_num[1]}
                Your Powerball: {ticket_num[1]}
            """

        return f"""
            You hit a match!
            The lottery Number was : {str_drawn_num}
            Your Winning Number was: {str_ticket_num} with {self.matches} matches!
            You bought {self.money_spent/self.cost} tickets.\n
            .\n
            {pb_result_text}
            .\n
            Money Stats:
            Spent   : ${self.money_spent}
            Winnings: ${earnings}
            Profit  : ${profit}

            You could buy roughly {int(profit/1.86)} eggs with that money!
        """


def main():
    while True:
        try:
            match_thresh = int(input("Thank you for playing the lottery! How many numbers are you trying to match? 1-5\n"))
            pb = int(input("Would you like to buy the powerball?\n 1 for true 2 for false")) + 1
            break
        except ValueError:
            print("Please enter a valid option. Each answer must be numbers.\n")
            continue

    lotto_roll = Lotto(match_thresh, pb)
    print(f"Your number is {lotto_roll.drawn_num}")

    lotto_result = [False, False]
    try:
        while False in lotto_result:
            ticket_num = gen_ticket_num()
            lotto_result = lotto_roll.compare_nums(ticket_num)

            print(f"Your ticket number is {stringify_ticket_num(ticket_num[0])} {ticket_num[1]} with {lotto_roll.matches} match!")

        #lotto_result[1] == powerball result
        print(lotto_roll.winnings(ticket_num, lotto_result[1]))

    except KeyboardInterrupt:
        print(f"""\nThe starting number was:{lotto_roll.drawn_num}\n
        You bought {lotto_roll.money_spent/lotto_roll.cost} lotto tickets and spent ${lotto_roll.money_spent}.
        """)




main()
