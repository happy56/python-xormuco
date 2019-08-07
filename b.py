"""
	Question B 
	---------------------------------------------------------------------------------------------
	The goal of this question is to write a software library that accepts 2 version string as input 
	and returns whether one is greater than, equal, or less than the other. 
	As an example: '1.2' is greater than '1.1'. Please provide all test cases you could think of.
	---------------------------------------------------------------------------------------------
"""

def get_value(ver, dots):
	arr = ver.split('.')
	sum = 0 
	for i in arr:
		sum += int(i) * 10 ** dots
		dots -= 1
	return sum 

def compa(a, b):
	dots = max(a.count('.'), b.count('.'))

	a_int = get_value(a, dots)
	b_int = get_value(b, dots)

	if a_int == b_int:
		return 'equal'
	if a_int > b_int:
		return 'greater'

	return 'less'

