"""Module providingFunction printing python version."""
from array import array
# Programming - Tip Calculator App
print("This app without GUI will assist you with splitting your receipt by each person with tips.") 

print("\n")
greeting = print('Welcome to the tips and payments calculator :)')
total_bill = float(input(f"What was the total bill? \nUse a dot for decimals $"))
tip_percent = int(
    input('How much tip percent would you like to give? ')) / 100
tip_amount = round(float(total_bill * tip_percent), 2)
print(f"This is your tip {tip_amount}")
people_to_pay = int(input('How many people to split the bill? \nUse 1 if only for yourself '))


def payment_per_person():
    """A dummy docstring."""
    how_to_pay = input(
        "Do you want to split the bill equally or no? \nyes or no? Use yes only for yourself\n")
    while True:
        if how_to_pay != "yes" and how_to_pay != "no":
            how_to_pay = input("Please choose between yes and no ")
        else:
            break
    if how_to_pay == "yes":
        payment = round((total_bill / people_to_pay * (1 + tip_percent)), 2)
        print(f"Each person should pay: {payment}")
    else:
        names_list = []
        spent_list = []
        i = 0
        n_step = 0
        while i < people_to_pay:
            line = 1
            print("Enter your names one by one")
            user_name = input("What is your name? ")
            input_prices = input(f"Enter {user_name}'s meal prices separated by space. Use a dot for decimals \n")
            prices_list = input_prices.split()
            print('Prices: ', prices_list)
            for p in range(len(prices_list)):
                prices_list[p] = float(prices_list[p])
            print(f"Sum of {user_name}'s = ", sum(prices_list))
            names_list.append(user_name)
            spent_list.append(sum(prices_list))
            i += 1
        calc_totals_rounded = [round(item, 2) for item in spent_list]
        print("Totals one by one ", calc_totals_rounded)
        #spent_list = list(map(int, spent_list))
        total = sum(spent_list)
        print("Total bill without tips ", total)
        if total < total_bill:
            print("Inserted spendings are less than a total bill.")
            print("Please, check the receipts and start again")
        elif total > total_bill:
            print("Inserted spendings are less than a total bill.")
            print("Please, check the receipts and start again")
        else:
            calc_tips_simple = [item * (1 + tip_percent) for item in spent_list]
            calc_tips_rounded = [round(item, 2) for item in calc_tips_simple]
            print("Totals with tips one by one ", calc_tips_rounded)
            print("Total bill with tips", sum(calc_tips_rounded))
        m_step = 0
        while m_step < people_to_pay:
            for (a_item, b_item) in zip(names_list, calc_tips_rounded):
                print(f"Dear {a_item}, you should pay {b_item} ")
                m_step += 1
            break


payment_per_person()
