import os
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
days={'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thrusday': 3, 'Friday': 4, 'Saturday':5,'Sunday':6, 'All':7}
days_str={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thrusday', 4:'Friday', 5:'Saturday', 6:'Sunday', 7:'All'}
months={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'All':13}
months_str={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',13:'All'}

def get_filters():# Taking input from the user and filtering the data on that basis
    cities=['Chicago','Washington','New York']
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(1):
        city=input("Enter the name of the city (Chicago / New York / Washington ) to explore the statistics:  ")
        if city.title() not in cities:
            print('Sorry, you entered the wrong input \n kindly enter Chicago / New York / Washington \n')

        elif city.lower()== 'chicago':
            city='chicago.csv'
            break
        elif city.lower() == 'new york':
            city='new_york_city.csv'
            break
        else:
            city='washington.csv'
            break

    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while(1):
        #months1=['January','February','March','April','May','June']
        month_str=input("Enter the month for which you want to explore the statistics\n(All, January, February, March, April, May or June): ")
        month_str=month_str.title()
        if month_str not in months:# here monthhs is a global variable and we are checking whether the input lies in it or not
            print('Sorry, you entered the wrong input \n kindly enter the right month as listed below\n')
        elif month_str!='All':
            month=months[month_str]
            break
        else:
            month='All'
            break
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)+
    
    while(1):
        day_str=input("Enter the particular day or All for which you want to see the statistics\n(All, Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday): ")

        day_str=day_str.title()
        if day_str not in days:
            print('Sorry, you entered the wrong input \n kindly enter the correct day again as listed below\n')
        elif day_str!='All':
            day=days[day_str]
            break
        else:
            day='All'
            break

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
    print("\n\nLoading Data.......\n\n")
    df=pd.read_csv(city)
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    if month!="All":
        df=df[df['month']==month]
    df['day_of_week']=df['Start Time'].dt.dayofweek
    
    if(day!='All'):
        df=df[df['day_of_week']==day]

    print('*'*40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['Start Time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))'''
    value=df['month'].mode()[0]
    #print(value)# GIVES THE INTEGER VALUE OF THE MOST COMMON MONTH
    #month_str=[key for key,v in months.items() if v == value]
    # GIVES THE STRING VALUE OF THE MONTH IN THE FORM OF LIST OF 1 ELEMENT.

    print('The most popular month of Travel is {}.\n'.format(months_str[value]))

    # TO DO: display the most common day of week
    value=df['day_of_week'].mode()[0]
    print('The most popular day of the week on which people travel is {0}({1}).\n'.format(days_str[value],value))

    # TO DO: display the most common start hour
    print('The most common starting hour is {} hrs( in 24 Hours Format ).'.format(str(df['Start Time'].dt.hour.mode().iloc[0])))

    print("\nThis took {} time to calculate.".format(str(time.time()-start_time)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station=df['Start Station'].mode()[0]
    print('The Most popular start_station is {}.\n'.format(pop_start_station))

    # TO DO: display most commonly used end station
    pop_end_station=df['End Station'].mode()[0]
    print('The Most popular end_station is {}.\n'.format(pop_end_station))
    df['Journey']=df['Start Station']+' to '+ df['End Station']
    pop_Journey_station=df['Journey'].mode()[0]
    
    # TO DO: display most frequent combination of start station and end station trip
    print("The most popular Journey is from {}. \n".format(pop_Journey_station))


    print("\nThis took %s seconds to calculate." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    minutes, seconds = divmod(total_travel_time, 60)
    hours, minutes = divmod(minutes, 60)
    print("The total time travelled is {0} hours, {1} minutes, and {2} seconds.\n".format(hours,minutes,seconds))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    minutes, seconds = divmod(mean_travel_time, 60)
    hours, minutes = divmod(minutes, 60)
    print("The mean travelled time is {0} hours, {1} minutes, and {2} seconds.\n".format(hours,minutes,seconds))

    print("\nThis took %s seconds to calculate." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count=df['User Type'].value_counts()
    print("Counts of User Types are as follows:\n\n{}\n".format(user_type_count))

    # TO DO: Display counts of gender
    if('Gender' in df.columns):
        gender_count=df['Gender'].value_counts()
        print("Counts of Gender Types are as follows: \n\n{}\n".format(gender_count))
    else:
        print('\nGender data is not available in the file\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df.columns):
        yob=df['Birth Year'].dropna()#Here we are dropping the birth year which is null
        print('The earliest year (the oldest person) of birth is {}\n'.format(int(yob.min())))
        print('The most recent year (the youngest person) of birth is {}\n'.format(int(yob.max())))
        print('The most common year of birth is {}\n'.format(int(yob.mode()[0])))
    else:
        print('\nBirth Year data is not available in the file\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    
    city, month, day = get_filters()
    df = load_data(city, month, day)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    

    #Asks the user wheter to display the 5 rows data at once and again asks for the next five rows from the user till the user enters other than 'yes' as input
    y=1
    upper=-5
    lower=0
    while(True):
       
        disp = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        while(disp.lower()=='yes'):
            upper+=5
            lower+=5
            print(df[df.columns[0:-1]].iloc[upper:lower])
            if(y==1):
                print("month column: ",end="")
                print(days_str,end="\n\n")
                print("days_of_week column: ",end="")
                print(months_str,end="\n\n")
                y=0
            disp = input('\nWould you like to view more individual trip data? '
                    'Type \'yes\' or \'no\'.\n')
        if(disp.lower()!='yes'):
            break
        
        
        
             
#Asking the user whether he/she wants to reuse the Applicaion.
    while(True):
        restart = input('\nWould you like to restart? Enter yes to restart or any other key to terminate\n')
        if restart.lower() != 'yes':
            break
        else:
            #To clear the screen if the user again wants to use the 
            os.system('cls' if os.name == 'nt' else 'clear')
            main()


if __name__ == "__main__":
	main()
 