"""
Project Euler Problem 19: Counting Sundays
"""

__author__ = "Benjamin R. Metzger"

DAYS_IN_MONTH: list = [
    31, #January
    28, #February
    31, #March
    30, #April
    31, #May
    30, #June
    31, #July
    31, #August
    30, #September,
    31, #October
    30, #November
    31 #December
]

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    date: int = 2
    sundays: int = 0

    for year in range(1901, 2001):
        for month in range(12):
            days: int = DAYS_IN_MONTH[month]
            if month == 1 and is_leap_year(year):
                days += 1
            date += days
            date %= 7
            if date == 0:
                sundays += 1

    print(sundays)            

if __name__ == "__main__":
    main()