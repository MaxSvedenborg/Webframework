from datetime import datetime, timedelta

# Various helper functions. Formating, datetime helpers etc.


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')


def divider():
    print('-' * 150)


def nextdate(date1, span=1):
    """
    Calculates next date
    :param datetimeobject:
    :param span: int (number of days from datetimeobject
    :return: dt1 and dt2; two datetime objects from 00:00:00 to 23:59:59
    """
    d1 = date1.replace(hour=0, minute=0, second=0, microsecond=0)
    d2 = d1 + timedelta(days=span)
    d2 = date1.replace(hour=23, minute=59, second=59, microsecond=0)
    return d1, d2


def date_sequence(date1,date2):
    """
    Creates a time series as a list of tuples where each date is a binary set starting at 00:00:00 and ends inn 23:59:59
    :param date1: datetime object
    :param date2: datetime object
    :return: list of tuples
    """
    # calculate the number of days between the dates
    # loop through sequence and add each tuple to a list
    # return the list


def main():
    date = datetime.now()
    print(nextdate(date, 1))


if __name__ == '__main__':
    main()