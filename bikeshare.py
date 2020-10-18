#This code will prompt data regardind the bikeshare project for the specified city, month and weekday

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Choose a city:')).lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print('Wrong city name. Choose among Chicago, New York City and Washington')
        city = str(input('Choose a city:')).title()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input('Choose a month to filter data or choose them all:')).title()
    while month not in ['January', 'February', 'March','April', 'May', 'June','July', 'August', 'September','October', 'November', 'December','All']:
        print('Wrong month name. Mind typos')
        month = str(input('Choose a month to filter data:')).title()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Choose a day to filter data or choose them all:')).title()
    while day not in ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday','Sunday','All']:
        print('Wrong day name. Mind typos')
        day = str(input('Choose a day to filter data:')).title()

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
    df['Day'] = df['Start Time'].dt.weekday_name
    
    if month != 'All':
        months = ['January', 'February', 'March','April', 'May', 'June','July', 'August', 'September','October', 'November', 'December']        
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'All':
        df = df[df['Day'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month is {}'.format(df['Month'].mode()))

    # TO DO: display the most common day of week
    print('\nThe most common day is {}'.format(df['Day'].mode()))

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print('The most common hour is {}'.format(df['Hour'].mode()))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is {}\n'.format(df['Start Station'].mode()))

    # TO DO: display most commonly used end station
    print('The most common end station is {}\n'.format(df['End Station'].mode()))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Stations'] = df['Start Station'] + ' and ' + df['End Station']
    print('\nThe most common start and end station combination is {}'.format(df['Start End Stations'].mode()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is {} seconds\n'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The average travel time is {} seconds\n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The type of users and its count are the following:\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('The gender of  the users and its count are the following:\n',df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\n The earliest birthyear is', int(df['Birth Year'].min()))
    print('\n and the most recent is', int(df['Birth Year'].max()))
    print('\n whereas the most common is ', int(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()