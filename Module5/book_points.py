# Module 5 CTA Part 2
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
#
# By: Melissa Hidalgo 352865

books = input('How many books did you purchase this month? ')
while not books.isdigit():
    books = input('Please enter a valid integer: ')

books = int(books)
points = 0

points = 0 if books <= 1 else 5 if books < 4 else 15 if books < 6 else 30 if books < 8 else 60

print('\nYou\'ve earned {} points this month!'.format(points))