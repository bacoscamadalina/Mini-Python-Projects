'''
                                                     - WATER METER -
There is a desire to implement an application for managing readings of hot and cold water meters for a family.
Every month, a family needs to submit the values of hot and cold water meters to the administrator, along with the
consumption for the current month. The goal is to simplify this activity through an application with the following
functionalities:
Add - reading for a specific month
Delete - reading for a specific month
Display consumption - for a specific month
Exit
When adding a reading, the user must enter the year and month in the format Jan, Feb, Mar, ... Dec, followed by the
values of the cold water meter and hot water meter. The user will receive an error message if the year or month is
incorrect, if there is already a reading for that month, or if the meter values are invalid (the current meter value
is less than the value of the previous month).
When deleting a reading, the user must enter the year and month. An error message will be received if the year and
month are invalid or if there is no reading for the entered year and month.
For display, the values of the meters for the previous and current month will be shown, along with the consumption for
the current month, for example:
Jan 2018
Hot water 100
Cold water 105
Feb 2018 consumption
104 4
110 5
When entering the months, the program should be case-insensitive, meaning both "feb" and "FEB" mean the same thing.
The value of the year does not need to be validated in any way.
Data does not need to be saved in a way that persists after the program is stopped.
'''


from collections import defaultdict

data = defaultdict(dict)

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def add_reading():
    year = input("Enter the year: ")
    month = input("Enter the month: ").lower()

    if month not in months:
        print("The month is not correct!")
        return

    if month in data[year]:
        print("Reading for the specified month already exists!")
        return

    cold_water = int(input("Enter the value of the cold water counter: "))
    hot_water = int(input("Enter the value of the hot water counter: "))

    if months.index(month) > 0:
        prev_month = months[months.index(month) - 1]
        if year in data and prev_month in data[year]:
            if cold_water < data[year][prev_month]['cold_water'] or hot_water < data[year][prev_month]['hot_water']:
                print("The value of the meters is invalid!")
                return

    data[year][month] = {'cold_water': cold_water, 'hot_water': hot_water}
    print("Reading successfully added!")

def delete_reading():
    year = input("Enter the year: ")
    month = input("Enter the month: ").lower()

    if month not in months or year not in data or month not in data[year]:
        print("There is no reading for the year and month you added!")
        return

    del data[year][month]
    print("Read successfully deleted!")

def show_consumption():
    year = input("Enter the year: ")
    month = input("Enter the month: ").lower()

    if month not in months or year not in data or month not in data[year]:
        print("There is no reading for the year and month you added!")
        return

    if months.index(month) > 0:
        prev_month = months[months.index(month) - 1]
        if year in data and prev_month in data[year]:
            cold_water_consumption = data[year][month]['cold_water'] - data[year][prev_month]['cold_water']
            hot_water_consumption = data[year][month]['hot_water'] - data[year][prev_month]['hot_water']
            print(f"{month} {year} consum")
            print(f"Cold water: {data[year][prev_month]['cold_water']} {cold_water_consumption}")
            print(f"Hot water: {data[year][prev_month]['hot_water']} {hot_water_consumption}")
        else:
            print("There is no reading for the previous month!")
    else:
        print("There is no reading for the previous month!")

def exit_app():
    print("Exit from the application.")
    exit(0)



actions = {
    '1': add_reading,
    '2': delete_reading,
    '3': show_consumption,
    '4': exit_app
}

while True:
    print("1. Add reading")
    print("2. Delete reading")
    print("3. Display consumption")
    print("4. Exit")

    action = input("Choose the option: ")
    actions.get(action, lambda: print("Invalid option!"))()


