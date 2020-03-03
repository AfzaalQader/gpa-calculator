from decimal import Decimal

def grades_points(percent):
	if percent >= 90 and percent <= 100:
		return 4.00
	elif percent >= 85 and percent <= 89.99:
		return 4.00
	elif percent >= 80 and percent <= 84.99:
		#return 3.66 - 3.99
		if percent >= 83 and percent <= 84.99:
			return 3.99
		elif percent >= 82 and percent <= 82.99:
			return 3.88
		elif percent >= 81.05 and percent <= 81.99:
			return 3.77
		elif percent >= 80 and percent <= 81.04:
			return 3.66
	elif percent >= 75 and percent <= 79.99:
		#return 3.33 - 3.65
		if percent >= 78 and percent <= 79.99:
			return 3.65
		elif percent >= 77 and percent <= 78.99:
			return 3.55
		elif percent >= 77.05 and percent <= 77.99:
			return 3.45
		elif percent >= 76.05 and percent <= 77.04:
			return 3.35
		elif percent >= 75 and percent <= 76.04:
				return 3.33
	elif percent >= 71 and percent <= 74.99:
		#return 3.00 - 3.32
		if percent >= 74 and percent <= 74.99:
			return 3.32
		elif percent >= 73 and percent <= 73.99:
			return 3.25
		elif percent >= 72 and percent <= 72.99:
			return 3.10
		elif percent >= 71 and percent <= 71.99:
			return 3.00
	elif percent >= 68 and percent <= 70.99:
		#return 2.66 - 2.99
		if percent >= 70 and percent <= 70.99:
			return 2.99
		elif percent >= 69.50 and percent <= 69.99:
			return 2.85
		elif percent >= 68.50 and percent <= 69.49:
			return 2.75
		elif percent >= 68.00 and percent <= 68.49:
			return 2.66
	elif percent >= 61 and percent <= 67.99:
		#return 2.00 - 2.65
		if percent >= 67.00 and percent <= 67.99:
			return 2.65
		elif percent >= 65.98 and percent <= 67.00:
			return 2.52
		elif percent >= 64.78 and 65.97:
			return 2.39
		elif percent >= 63.58 and percent <= 64.77:
			return 2.26
		elif percent >= 62.58 and percent <= 63.57:
			return 2.13
		elif percent >= 61.00 and percent <= 62.57:
			return 2.99
	elif percent >= 50 and percent <= 60.99:
		#return 1.00 - 1.99
		if percent >= 59.00 and percent <= 60.99:
			return 1.90
		elif percent >= 58.00 and percent <= 58.99:
			return 1.80
		elif percent >= 57.00 and percent <= 57.99:
			return 1.70
		elif percent >= 56.00 and percent <= 56.99:
			return 1.60
		elif percent >= 55.00 and percent <= 55.99:
			return 1.50
		elif percent >= 54.00 and percent <= 54.99:
			return 1.40
		elif percent >= 53.00 and percent <= 53.99:
			return 1.30
		elif percent >= 52.00 and percent <= 52.99:
			return 1.20
		elif percent >= 51.00 and percent <= 51.99:
			return 1.15
		elif percent >= 50.00 and percent <= 50.99:
			return 1.00
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