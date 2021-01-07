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
    d2 = d2.replace(hour=23, minute=59, second=59, microsecond=0)
    return d1, d2


def date_sequence(date1, date2):
    """
    Creates a sequence as a list of tuples where each tuple is a set of
    date objects starting at X-X-X 00:00:00 and ends at Y-Y-Y 23:59:59
    :param date1: datetime object
    :param date2: datetime object
    :return: list of tuples
    """
    delta = date2 - date1
    sequence = []
    i = 1
    date = date1
    while i <= delta.days:
        d1, d2 = nextdate(date, 0)
        dates = (d1, d2)
        sequence.append(dates)
        date += timedelta(days=1)
        i += 1
    return sequence


def main():
    date = datetime.now()
    d1, d2 = nextdate(date, 3)
    diff = date_sequence(d1, d2)
    for dateseq in diff:
        print(dateseq[0], '-', dateseq[1])


if __name__ == '__main__':
    main()
