"""Module providingFunction printing python version."""
# Programming - Tip Calculator App 

print("\n")
greeting = print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
tip_percent = int(
    input('How much tip percent would you like to give? ')) / 100
tip_amount = round(float(total_bill * tip_percent), 2)
print(f"This is your tip {tip_amount}")
people_to_pay = int(input('How many people to split the bill ? '))


def payment_per_person():
    """A dummy docstring."""
    how_to_pay = input(
        "How do you want to split the bill equally or no? yes or no?\n")
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
            user_name = input("What is your name? ")
            input_prices = input(f'Enter {user_name} meal prices separated by space ')
            prices_list = input_prices.split()
            print('Prices: ', prices_list)
            for p in range(len(prices_list)):
                prices_list[p] = int(prices_list[p])
            print(f"Sum of {user_name} = ", sum(prices_list))
            names_list.append(user_name)
            spent_list.append(sum(prices_list))
            i += 1
        print("Totals one by one ", spent_list)
        spent_list = list(map(int, spent_list))
        total = sum(spent_list)
        print("Total bill without tips ", total)
        if total < total_bill:
            print("Inserted spendings are less than a total bill.")
            print("Please, check the receipts again")
        elif total > total_bill:
            print("Inserted spendings are less than a total bill.")
            print("Please, check the receipts again")
        else:
            calc_simple = [item * (1 + tip_percent) for item in spent_list]
            calc_rounded = [round(item, 2) for item in calc_simple]
            print("Totals with tips one by one ", calc_rounded)
            print("Total with tips", sum(calc_rounded))
        m_step = 0
        while m_step < people_to_pay:
            for (a_item, b_item) in zip(names_list, calc_rounded):
                print(f"Dear {a_item}, you should pay {b_item} ")
                m_step += 1
            break


payment_per_person()
