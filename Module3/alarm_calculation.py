# Module 3 CTA Part 2: 
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.
#
# By: Melissa Hidalgo 352865

# Function to check if the user entered hour is a valid input
def validate_hour(string):
    if(not string.isdigit()):
        return False
    if(int(string) > 23 or int(string) < 0):
        return False
    
    return True

def set_alarm(current_hour, hours_from_now):
    hours_passed = current_hour + hours_from_now
    return hours_passed % 24

hour_str = input('Enter the current hour between 0 and 23: ')

# Make sure entry is valid
while not validate_hour(hour_str):
    hour_str = input('Invalid entry. Please enter the hour as an integer between 0 and 23: ')

hour = int(hour_str)

alarm_hours_str = input('Enter the number of hours from now that you would like to set an alarm for: ')

while not alarm_hours_str.isdigit():
    alarm_hours_str = input('Invalid entry. Please enter a whole number')

alarm_hours = int(alarm_hours_str)

time_on_clock = set_alarm(hour, alarm_hours)
print('It will be', time_on_clock, 'when your alarm goes off')