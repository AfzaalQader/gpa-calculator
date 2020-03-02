from decimal import Decimal

def grades_points(percent):
	if percent >= 90 and percent <= 100:
		return 4.00
	elif percent >= 85 and percent <= 89.99:
		return 4.00
	elif percent >= 80 and percent <= 84.99:
		#return 3.66 - 3.99
		return 3.87
	elif percent >= 75 and percent <= 79.99:
		#return 3.33 - 3.65
		return 3.6
	elif percent >= 71 and percent <= 74.99:
		#return 3.00 - 3.32
		return 3.31
	elif percent >= 68 and percent <= 70.99:
		#return 2.66 - 2.99
		return 2.68
	elif percent >= 61 and percent <= 67.99:
		#return 2.00 - 2.65
		return 2.5
	elif percent >= 50 and percent <= 60.99:
		#return 1.00 - 1.99
		return 1.12
	elif percent < 50:
		return 0.00


def gpa_calculator(subject,total_marks,obtain_marks,cridet_hours):
	percentage_mark = round((obtain_marks / total_marks) * 100.00 , 2)
	subject_gpa = grades_points(percentage_mark)
	quality_point = subject_gpa * cridet_hours
	return quality_point
	



print('Welcome to GPA Calculator')
isMoreAdd = 'y'
c = 1
sum_of_quality_point = 0
sum_of_cridet_hours = 0
while isMoreAdd == 'Y' or isMoreAdd == 'y':
	subject = input('Please Enter Subject Name:  ')
	total_marks = int(input('Please enter total marks of subject {}:  '.format(subject)))
	obtain_marks = float(input('Please enter obtain marks of subject {}:  '.format(subject)))
	if obtain_marks < 0 or obtain_marks > total_marks:
		print('Please Enter valid obtain marks of subject {}:  '.format(subject))
		obtain_marks = float(input('Please enter obtain marks of subject {}:  '.format(subject)))
	cridet_hours = int(input('Please enter cridet hours of subject {}:  '.format(subject)))
	sum_of_quality_point += gpa_calculator(subject,total_marks,obtain_marks,cridet_hours)
	sum_of_cridet_hours += cridet_hours
	print('You have been added Successfully {} Subjects'.format(c))
	isMoreAdd = input('Do you add more subject ? Y / N : ???')
	c += 1

gpa = sum_of_quality_point / sum_of_cridet_hours
print('Your Semester GPA is {} '.format(gpa))