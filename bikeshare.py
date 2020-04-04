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
    print('Hello and welcome! Let\'s explore this wonderful US bikeshare database!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter any desired city from the three available (chicago, new york city, washington)\n').lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
        city = ('Invalid input. Please choose only from the available cities').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter the month name whose data you wish to explore (type \'all\' to select all months or a particular month name to choose any month between january and june)\n').lower()
    
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = ('Invalid input. Please choose only from the avilable months').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day of the week whose data you wish to explore (type \'all\' to select all days or a particular day name to choose any particular day)\n').lower()
    
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        day = ('Invalid input. Please choose only from the avilable months').lower()


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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.dayofweek
    
    
    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month in months:
            month = months.index(month) + 1
            df = df[df['Month'] == month] 
    
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day in days:
            day = days.index(day)
            df = df[df['Day'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {}'.format(str(df['Month'].mode().values[0])))
    print('(January = 1, February = 2, March = 3, April = 4, May = 5, June = 6)\n')
    # TO DO: display the most common day of week
    print('The most common day of the week is: {}'.format(str(df['Day'].mode().values[0])))
    print('(Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6)\n')
    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: {}'.format(str(df['Hour'].mode().values[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Routes'] = df['Start Station'] + ' - ' + df['End Station']
    print('The most common bike route is: {}'.format(df['Routes'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['Trip Time'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print('The total travel time is: {}'.format(str(df['Trip Time'].sum())))

    # TO DO: display mean travel time
    print('The average travel time is: {}'.format(str(df['Trip Time'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    

    # TO DO: Display counts of user types
    df1 = df['User Type'].value_counts()
    print('The counts for each type of users:\n')
    print(df1)
    # TO DO: Display counts of gender
    if city != 'washington':
        df2 = df['Gender'].value_counts()
        print('The counts for each type of genders:\n')
        print(df2)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('The earliest birth year for any user is: {}'.format(str(int(df['Birth Year'].min()))))
        print('The latest birth year for any user is: {}'.format(str(int(df['Birth Year'].max()))))
        print('The most common birth year for any user is: {}'.format(str(int(df['Birth Year'].mode().values[0]))))
    
    print("\nThe amount of time taken")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    """
    Display contents of the CSV file to the display if it's requested by
    the user.
    
    """

    start = 0
    end = 5

    display1 = input("Do you want to see the raw data? (yes/no): ").lower()

    if display1 == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end])
            start += 5
            end += 5

            display2 = input("Do you wish to continue? (yes/no): ").lower()
            if display2 == 'no':
                break    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
