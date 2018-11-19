from secrets import randbelow


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

        self.pb_cost  = powerball
        self.pb_bool = True if powerball == 3 else False

        self.drawn_num = gen_ticket_num()
        self.money_spent = 0


    def compare_nums(self, ticket_num):
        #comppare ticket numbers
        self.matches = 0
        results = []

        for num in ticket_num[0]:
            if num in self.drawn_num[0]:
                self.matches += 1

        results.append(True if self.matches >= self.match_threshold else False)

        self.money_spent += 2
        #check powerball results
        self.pb_bool
        if self.pb_bool:
            self.money_spent += 1
            results.append(True if self.drawn_num[1] == ticket_num[1] else False)


        return results



def main():
    while True:
        try:
            match_thresh = int(input("Thank you for playing the lottery! How many numbers are you trying to match? 1-5\n"))
            pb = int(input("Would you like to buy the powerball?\n 1 for true 2 for false")) + 1
            break
        except ValueError:
            print("Please enter a valid option. Each answer must be numbers.")
            continue

    lotto_roll = Lotto(match_thresh, pb)
    print(f"Your number is {lotto_roll.drawn_num}")

    lotto_result = [False, False]

    while False in lotto_result:
        ticket_num = gen_ticket_num()
        lotto_result = lotto_roll.compare_nums(ticket_num)

        print(f"Your ticket number is {ticket_num} with {lotto_roll.matches} match!")

    print(lotto_result)



main()

# def gen_lottery_number(pb):
#     nums = []
#     total = 0
#
#     while total <= 5:
#         nums.append(randbelow(69))
#         total += 1
#
#     if pb == 3:
#         nums.append(randbelow(29))
#
#     return nums
#
#
# def winnings():
#     rewards_dict = {
#         "True": {
#             1: 4,
#             2: 7,
#             3: 100,
#             4: 50000,
#             5: 124000000
#         },
#         "False": {
#             1: 4,
#             2: 4,
#             3: 7,
#             4: 100,
#             5: 1000000
#         }
#     }
#
#     return True
#
#
# def get_inputs():
#     while True:
#         try:
#             match_thresh = int(input("Thank you for playing the lottery! How many numbers are you trying to match? 1-5\n"))
#             pb = int(input("Would you like to buy the powerball?\n 1 for true 2 for false")) + 1
#             break
#         except ValueError:
#             print("Please enter a valid option. Each answer must be numbers.")
#             continue
#
#     return match_thresh, pb
#
#
# def main():
#     money_spent = 0
#     ticket_num = 0
#
#     match_thresh, pb = get_inputs()
#     rolled_numbers = gen_lottery_number(pb)
#
#     try:
#         while matches < match_thresh:
#             money_spent += pb
#             pb_result = False
#             matches = 0
#             ticket_num = gen_lottery_number(pb)
#
#             for num in ticket_num:
#                 try:
#                     if ticket_num.index(num) != len(ticket_num) -1 and rolled_numbers.index(num) != len(rolled_numbers) -1:
#                         matches += 1 if num in rolled_numbers else 0
#                 except:
#                     pass
#
#             if pb == 3 and rolled_numbers[-1] == ticket_num[-1]:
#
#
#     except KeyboardInterrupt:
#         print(f"""\nThe starting number was:{rolled_numbers}\n
#         You bought {money_spent/pb} lotto tickets and spent ${money_spent}.
#         """)
