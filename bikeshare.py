import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
pd.set_option("max_columns", 15)
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
    print()
    cities = {'ch':'chicago' , 'ny':'new york city' , 'wa':'washington' } # dictionary to connect the inputed shortcuts with the real strings
    while True:
        city = input('Enter City Name (NY for New York, CH for Chicago WA for Washington) : ')
        city = city.lower().strip() #in case the user inputs in capital letters / adds spaces by mistake
        if city in cities.keys()  : #if the input matches available data, the program gets out of the while loop
            city = cities[city]
            print('You\'ve chosen {}'.format(city.capitalize()))
            break
        elif city in cities.values() :
            print('You\'ve chosen {}'.format(city.capitalize()))
            break
        else :
            print('Unrecognized input , please try again.')
            print()

    # TO DO: get user input for month (all, january, february, ... , june)
    print()
    months ={'jan':'january' , 'feb':'february' , 'mar':'march' , 'apr':'april', 'may':'may' , 'jun':'june' , 'all':'all'} # dictionary to connect the inputed shortcuts with the real strings
    while True:
        month = input('Enter Month (Jan , Feb , Mar , Apr , May , Jun or All) : ')
        month = month.lower().strip() #in case the user inputs in capital letters / adds spaces by mistake
        if month in months.keys()  : #if the input matches available data, the program gets out of the while loop
            month = months[month]
            print('You\'ve chosen {}'.format(month.capitalize()))
            break
        elif month in months.values():
            print('You\'ve chosen {}'.format(month.capitalize()))
            break
        else :
            print('Unrecognized input , please try again.')
            print()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print()
    days ={ 'fri':'friday' ,'sat':'saturday' , 'sun':'sunday' , 'mon':'monday' , 'tue':'tuesday' , 'wed':'wednesday' , 'thu':'thursday', 'all':'all'} # dictionary to connect the inputed shortcuts with the real strings
    while True:
        day = input('Enter day Name (Fri , Sat ,  Sun , Mon , Tue , Wed , Thu or all) : ')
        day = day.lower().strip() #in case the user inputs in capital letters / adds spaces by mistake
        if day in days.keys() : #if the input matches available data, the program gets out of the while loop
            day = days[day]
            print('You\'ve chosen {}'.format(day.capitalize()))
            break
        elif day in days.values():
            print('You\'ve chosen {}'.format(day.capitalize()))
            break
        else :
            print('Unrecognized input , please try again.')
            print()

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']

        # filter by month to create the new dataframe
        df = df[df['month'] == months.index(month) + 1]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    ########## display the most common month ##########

    # find the most popular month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month = df['month'].mode()[0]
    print('Most Popular Start month:', months[popular_month-1]) # [popular_month-1] just to match list indexing (starts from 0)

    ########## display the most common day of week ##########

    # find the most popular hour
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)

    ########## display the most common start hour ##########

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] +' >>> '+ df['End Station'] # a trip starts from starting station and ends at end station. logic :)
    popular_trip = df['trip'].mode()[0]
    print('Most Frequent Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duaration = df['Trip Duration'].sum()
    print('Total Travel Time: {} seconds'.format(total_trip_duaration))
    print('                 = {} minutes'.format(total_trip_duaration/60)) # 1 minute = 60 seconds
    print('                 = {} hours'.format(total_trip_duaration/60/60)) # 1 hour = 60 minutes
    print()

    # TO DO: display mean travel time
    mean_trip_duaration = df['Trip Duration'].mean()
    print('Mean Travel Time: {} second'.format(mean_trip_duaration))
    print('                = {} min'.format(mean_trip_duaration/60)) # 1 minute = 60 seconds

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Subscribers: ',user_types['Subscriber'])
    print('Customers:   ',user_types['Customer'])
    print()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns : # Gender data is only available in new_york_city and chicago
        Genders = df['Gender'].value_counts()
        print('Male:   ',Genders['Male'])
        print('Female: ',Genders['Female'])
    else :
        print('Sorry, no Gender data available in Washington')
    print()

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns : # Birth Year data is only available in new_york_city and chicago
        common_birth_year = df['Birth Year'].mode()[0]
        print('Common Birth Year: ',common_birth_year)

        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth Year (oldest): ',earliest_birth_year)

        recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year (youngest): ',recent_birth_year)

    else :
        print('Sorry, no Birth Year data available in Washington')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_input(df):

    # this function allows the user to see some raw data if he wants to
    df = df.drop(['trip', 'hour','month'], axis = 1) #removing unnecessary columns
    row_index=0 # the displayed row index
    while True :
        show_data = input ('\nWould you like to see some raw data? Enter yes or no.\n')
        if show_data.lower().strip() != 'yes':
            break
        else :
            print(df.loc[[row_index]])
            row_index +=1
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() != 'yes':
            break


if __name__ == "__main__":
	main()
