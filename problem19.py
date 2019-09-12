"""
You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""


# of course using datetime would make this even simpler


month_name = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]
day_name = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def month_length(month, year):
    if month==1:
        return 29 if is_leap(year) else 28
    elif month in (8, 3, 5, 10):
        return 30
    else:
        return 31


def months_starting_with_sundays_since_1900(end_year, verbose=False):
    # jan 1st, 1900
    count = 0
    first = 1
    for year in range(1900, end_year+1):
        for month in range(12):
            if verbose:
                print("{} 1/{}/{}".format(
                        day_name[first], month_name[month], year))
            if first == 0:
                count += 1
            first = (first + month_length(month, year)) % 7
    return count


def solution():
    return (months_starting_with_sundays_since_1900(2000) -
            months_starting_with_sundays_since_1900(1900))


if __name__ == '__main__':
    print('1902 {}'.format(
            months_starting_with_sundays_since_1900(1902, verbose=True)))
    print()
    for i in (1900, 2000):
        print('{} {}'.format(
                i, months_starting_with_sundays_since_1900(i)))
