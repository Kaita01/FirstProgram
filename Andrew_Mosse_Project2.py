# Andrew Mosse
# Project 2
# Assignment due: Jan 7, 2022
# COSC 1336
# Calculate the average high/low temp in both °F and °C over the 3 days, as well as the total rainfall in both inches and centimeters.

print('Enter the information for all 3 days')

# input/storage
day_A = input('Enter the day of the week (such as Monday)')

high_A = int(input('Enter the high temperature for the day (in °F)'))

low_A = int(input('Enter the low temperature for the day (in °F)'))

rainfall_A = int(input('Enter the amount of rainfall for the day (in inches)'))

day_B = input('Enter the day of the week (such as Monday)')

high_B = int(input('Enter the high temperature for the day (in °F)'))

low_B = int(input('Enter the low temperature for the day (in °F)'))

rainfall_B = int(input('Enter the amount of rainfall for the day (in inches)'))

day_C = input('Enter the day of the week (such as Monday)')

high_C = int(input('Enter the high temperature for the day (in °F)'))

low_C = int(input('Enter the low temperature for the day (in °F)'))

rainfall_C = int(input('Enter the amount of rainfall for the day (in inches)'))

# calculations
averagehigh = (high_A + high_B + high_C) / 3
averagelow = (low_A + low_B + low_C) / 3
totalrainfall = rainfall_A + rainfall_B + rainfall_C
averagehighC = (averagehigh - 32) * 5 / 9
averagelowC = (averagelow - 32) * 5 / 9
totalrainfallC = totalrainfall * 2.54

# output
print('For the last three days --', day_A, day_B, day_C)

print('Average High:%d°F'% averagehigh)

print('Average Low:%d°F'% averagelow)

print('Total rainfall:%s inches'% totalrainfall)

print('Average High:%d°C'% averagehighC)

print('Average Low:%d°C'% averagelowC)

print('Total rainfall:%s centimeters'% totalrainfallC)
