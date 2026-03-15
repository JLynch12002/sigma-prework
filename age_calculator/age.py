from datetime import datetime
from dateutil import relativedelta


def calculate_age():
    current_date = datetime.now()
    input_date = input("Enter a date [year-month-day]: ")
    while True:
        try:
            input_date = datetime.strptime(input_date, "%Y-%m-%d")
            break
        except:
            input_date = input(
                "Invalid Date. Try Again\nEnter a date [year-month-day]: ")

    date_diff = relativedelta.relativedelta(current_date, input_date).years

    if date_diff < 0:
        return print(f"{abs(date_diff)} Years Into The Future")
    else:
        return print(f"{date_diff} Year Difference")


calculate_age()
