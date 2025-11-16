# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import time
import calendar as cal
import sys


# Dictionary of data files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Global constants for months and days (Refactor 1: Moved to global scope)
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
VALID_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Welcome! Let's start exploring some US bikeshare data!\n")

    # Menu options, using global constants
    cities = ['chicago', 'new york city', 'washington']
    months = VALID_MONTHS + ['all']
    days = VALID_DAYS + ['all']

    # Helper function to get valid input
    def select_option(options, prompt):
        while True:
            for i, option in enumerate(options, 1):
                print(f"{i}. {option.title()}")
            choice = input(prompt).strip()
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(options):
                    return options[index]
            print(f"Invalid input. Please enter a number between 1 and {len(options)}.\n")

    print("Choose a city:")
    city = select_option(cities, "Enter number: ")

    print("\nChoose a month:")
    month = select_option(months, "Enter number: ")

    print("\nChoose a day:")
    day = select_option(days, "Enter number: ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday

    # Filter by month
    if month != 'all':
        # Using global constant VALID_MONTHS
        month = VALID_MONTHS.index(month) + 1
        df = df[df['Month'] == month]

    # Filter by day
    if day != 'all':
        # Using global constant VALID_DAYS
        day = VALID_DAYS.index(day)
        df = df[df['Weekday'] == day]

    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Most common month
    ind_month = df['Month'].value_counts().idxmax()
    if month != 'all':
        print('You have selected ',month.title(),', so, unsurprisingly, the most common '+
              'month in',city.title(),'is', cal.month_name[ind_month], ';) \n\n')
    else:
        print('The most common month in ',city.title(),' is',
              cal.month_name[ind_month], '.\n\n')

    # Most common day of week
    ind_day = df['Weekday'].value_counts().idxmax()
    if day != 'all':
        print('You have selected',day.title(),'so, unsurprisingly, the most common '+
              'day of the week in',city.title(),'is', cal.day_name[ind_day], ';) \n\n')
    else:
        print('The most common day of the week is', cal.day_name[ind_day], '\n\n')

    # Most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    print('The most common start hour for your selection is',
          df['Start Hour'].value_counts().idxmax(), 'o\'clock.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most common start station for your selection is',
          df['Start Station'].value_counts().idxmax(), '.\n\n')

    print('The most common end station for your selection is',
          df['End Station'].value_counts().idxmax(), '.\n\n')

    # Most common trip combination
    df['Station Combination'] = df['Start Station'] + ' (start) and ' + df['End Station'] + ' (end).'

    print('The most common station combination for your selection is ',
          df['Station Combination'].value_counts().idxmax(), '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Total travel time
    trip_sum_sec = df['Trip Duration'].sum()
    trip_sum_h = round(trip_sum_sec / 60 / 60 ,0)
    print('The total travel time for your selection is', trip_sum_h, 'hours.\n\n')

    # Mean travel time
    trip_mean_sec = df['Trip Duration'].mean()
    trip_mean_min = round(trip_mean_sec / 60 ,0)

    if trip_mean_min < 60:
        print('The mean travel time for your selection is', trip_mean_min, 'minutes.\n\n')
    else:
        trip_mean_h = round(trip_mean_min / 60 ,1)
        print('The mean travel time for your selection is', trip_mean_h, 'hours.\n\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users. Statistics will be calculated using NumPy."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # User Type Counts
    usertypes = df['User Type'].values
    ct_subscriber = (usertypes == 'Subscriber').sum()
    ct_customer = (usertypes == 'Customer').sum()

    print('The number of subscribers in', city.title(), 'is:',ct_subscriber,'\n')
    print('The number of customers in', city.title(), 'is:',ct_customer,'\n')

    if city.title() != 'Washington':
        # Gender Counts
        gender = df['Gender'].values
        ct_male = (gender == 'Male').sum()
        ct_female = (gender == 'Female').sum()

        print('The number of male users in', city.title(), 'is:',ct_male,'\n')
        print('The number of female users in', city.title(), 'is:',ct_female,'\n')

        # Birth Year Statistics (Refactor 2: Simplified birth year calculation)
        birthyear_data = df['Birth Year'].dropna()

        latest_birthyear = birthyear_data.max()
        earliest_birthyear = birthyear_data.min()
        most_common_birthyear = birthyear_data.value_counts().idxmax()

        print('The most recent birth year of users in', city.title(), 'is:',
              int(latest_birthyear) ,'\n')
        print('The earliest birth year of users in', city.title(), 'is:',
              int(earliest_birthyear),'\n')

        print('The most common birth year of users in', city.title(), 'is:',
              int(most_common_birthyear), '\n')

    else:
        print('Sorry. Gender and birth year information are not available for Washington!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays 5 lines of raw data at a time based on menu choice."""
    i = 0
    while True:
        print("\nWould you like to see 5 lines of raw data?")
        print("1. Yes, show next 5 rows")
        print("2. No, stop showing raw data")
        print("3. End program")

        choice = input("Enter number: ")

        if choice == "1":
            print(df[i:i+5])
            i += 5
            if i >= len(df):
                print("\nNo more data to display.")
                break
        elif choice == "2":
            break
        elif choice == "3":
            print("Thank you for using our program!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        raw_data(df)

        # Restart menu
        while True:
            print("\nWould you like to restart?")
            print("1. Yes")
            print("2. No")
            print("3. End program")
            restart_choice = input("Enter number: ")

            if restart_choice == "1":
                break  # go back to start of main loop
            elif restart_choice in ("2", "3"):
                print("Thank you for using our program!")
                sys.exit()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__": main()