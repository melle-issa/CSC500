# Module 5 CTA Part 1
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
# The program should first ask for the number of years. The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user 
# for the inches of rainfall for that month. After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.
#
# By: Melissa Hidalgo 352865

def convert_i_to_month(i):
    if i == 1:
        return 'January'
    elif i == 2:
        return 'February'
    elif i == 3:
        return 'March'
    elif i == 4:
        return 'April'
    elif i == 5:
        return 'May'
    elif i == 6:
        return 'June'
    elif i == 7:
        return 'July'
    elif i == 8:
        return 'August'
    elif i == 9:
        return 'September'
    elif i == 10:
        return 'October'
    elif i == 11:
        return 'November'
    else:
        return 'December'
    
def validate_input(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

years_str = input('How many years would you like to enter rainfall for? ')
while not years_str.isdigit():
    years_str = input('Please entere a valid integer for the number of years: ')

print()
years = int(years_str)
months = years * 12
total_rainfall = 0

for i in range(years):
    for j in range(12):
        month = convert_i_to_month(j + 1)
        monthly_rainfall = input('How many inches of rain was there in {} of year {}? '.format(month, i + 1))
        while not validate_input(monthly_rainfall):
            monthly_rainfall = input('Please enter a valid numerical form for the number of inches: ')
        total_rainfall += float(monthly_rainfall)
    print()

print('Total number of months: {}'.format(months))
print('Total rainfall: {:.3f}'.format(total_rainfall))
print('Average rainfall per month for the {} year period: {:.3f}'.format(years, total_rainfall / months))