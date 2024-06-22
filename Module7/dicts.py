# Module 7 CTA
# Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet
# The program should also create a dictionary containing course numbers and the names of the instructors that teach each course
# The program should also create a dictionary containing course numbers and the meeting times of each course
#
# By: Melissa Hidalgo 352865

def validate_course_number(course_number, room_numbers, instructors, meeting_times):
    valid = True
    if course_number not in room_numbers.keys():
        valid = False
    if course_number not in instructors.keys():
        valid = False
    if course_number not in meeting_times.keys():
        valid = False
    return valid

room_numbers = {'CSC101' : 3004, 'CSC102' : 4501, 'CSC103' : 6755, 'NET110' : 1244, 'COM241' : 1411}
instructors = {'CSC101' : 'Haynes', 'CSC102' : 'Alvarado', 'CSC103' : 'Rich', 'NET110' : 'Burke', 'COM241' : 'Lee'}
meeting_times = {'CSC101' : '8:00 a.m.', 'CSC102' : '9:00 a.m.', 'CSC103' : '10:00 a.m.', 'NET110' : '11:00 a.m.', 'COM241' : '1:00 p.m.'}

course_number = input('Please enter a course number to look up. Format should be AAA111: ')

if validate_course_number(course_number, room_numbers, instructors, meeting_times):
    room_number = room_numbers[course_number]
    instructor = instructors[course_number]
    meeting_time = meeting_times[course_number]

    print()
    print(course_number)
    print('Room number: {}'.format(room_number))
    print('Instructor: {}'.format(instructor))
    print('Meeing time: {}'.format(meeting_time))
else:
    print('\nClass not present in course catalog')