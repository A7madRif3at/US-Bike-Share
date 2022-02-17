import time
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt


CITY_DATA = { 'chicago': (r'C:\Users\admin\Downloads\Compressed\US Bike Share\chicago.csv'),
              'new york city': (r'C:\Users\admin\Downloads\Compressed\US Bike Share\new_york_city.csv'),
              'washington': (r'C:\Users\admin\Downloads\Compressed\US Bike Share\washington.csv')
              }

months = ['all','january', 'february', 'march', 'april', 'may', 'june']
week_day = ['all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']
    

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('which city to analyze, from the following chicago, new york city, washington: \n')
    city = city.lower()
    while city not in CITY_DATA:
        print ("INCCORECT ENTERY ,please try again")
        city = input('which city to analyze, from the following chicago, new york city, washington: \n')

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    both = input('would you like to filter the data by month, day, both, or not at all? type"none" for no time filter \n')
    if both == 'month':
        month = input('Please advice name of the month to filter by (january, february, march, april, may, june) \n')
        month = month.lower()
        while month not in months:
            print ("INCCORECT ENTERY ,please try again")
        
            month = input('name of the month to filter by (january, february, march, april, may, june) \n')
        day = ('all')
    elif both == 'day':
        day = input('name of the day of week to filter by (monday, tuesday, wednesday,thursday, friday, saturday, sunday)\n')
        day = day.lower()
        while day not in week_day:
            print ("INCCORECT ENTERY ,please try again")
            day = input('name of the day of week to filter by (monday, tuesday, wednesday,thursday, friday, saturday, sunday)\n')
        month = ('all')
    elif both == 'both':
        month = input('name of the month to filter by (january, february, march, april, may, june) \n')
        month = month.lower()
        while month not in months:
            print ("INCCORECT ENTERY ,please try again")
            month = input('name of the month to filter by (january, february, march, april, may, june) \n')
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('name of the day of week to filter by (monday, tuesday, wednesday,thursday, friday, saturday, sunday)\n')
        day = day.lower()
        while day not in week_day:
            print ("INCCORECT ENTERY ,please try again")
            day = input('name of the day of week to filter by \n')
    elif both == 'none':
        month = ('all')
        day = ('all')
    else:
        print('N/A in the choices \n ,we will sort all info for the selected city')
        month = ('all')
        day = ('all')                
    
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
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.strftime("%A")
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        
        month = months.index(month)
        df = df.loc[df['month'] == month]
    else:
        month == 'all'
        
    if day != 'all':
        df = df.loc[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month : " + months[common_month].title())

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print("The most common day: " + common_day)

    # TO DO: display the most common start hour
    start_hour = df['hour'].mode()[0]
    print("The most common start hour: " + str(start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_startstation = df['Start Station'].mode()[0]
    print('most commonly used start station ', most_startstation)

    # TO DO: display most commonly used end station
    most_endstation = df['End Station'].mode()[0]
    print('most commonly used end station ', most_endstation)
    # TO DO: display most frequent combination of start station and end station trip
    most_trafficstation = df[['Start Station', 'End Station']].max(axis=1)
    trafficstation = most_trafficstation.mode()
    print('most frequent combination of start station and end station trip ', trafficstation)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TTT = df['Trip Duration'].sum()
    print("Total Travel Time "+ str(TTT))

    # TO DO: display mean travel time
    ATT = df['Trip Duration'].mean()
    print("Average Travel Time "+ str(ATT))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts(dropna=False)
    print('counts of user types\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('counts of Gender\n', df['Gender'].value_counts(dropna=False))
    else:
        print('Gender informatation N/A for this selection \n')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Display earliest year of birth\n', df['Birth Year'].min())
        print('Most recent year of birth\n', df['Birth Year'].max())
        print('Most common year of birth\n', df['Birth Year'].mode())
    else:
        print('Birth Year informatation N/A for this selection')


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def rows(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes'.lower():
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
        
#def City_Share():
    #TD = pd.read_csv(CITY_DATA['chicago'])
    #TD1 = pd.read_csv(CITY_DATA['new york city'])
    #TD2 = pd.read_csv(CITY_DATA['washington'])
    #CTD = ("Chicago", TD['Trip Duration'].sum()), ("New York City", TD1['Trip Duration'].sum()), ("Washington", TD2['Trip Duration'].sum())
    #Total= TD['Trip Duration'].sum() + TD1['Trip Duration'].sum() + TD2['Trip Duration'].sum()
    #perc = [TD['Trip Duration'].sum()/Total,
        #TD1['Trip Duration'].sum()/Total,
        #TD2['Trip Duration'].sum()/Total
        #]
    #plt.title('Total Trip Actual City Share')
    #plt.axis('equal')
    #explode = (0, 0,0.3)
    #plt.pie(perc, labels = {'chicago', 'new york city', 'washington'}, autopct='%1.2f%%', startangle=90, explode=explode)
    #City_Share = input('Would you like to see Total Trip City Actual Share ')
    #if City_Share == 'yes':
        #plt.show()

#def  Total_Trip(df):
    #Trip = df.groupby('month')[['Trip Duration']].sum()
    #Trip.plot()
    #plt.title('Total Trip for Each Month')
    #plt.show()    

def main():

    while True:
        #City_Share()
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #Total_Trip(df)
        rows(df)
        
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
