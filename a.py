"""
	Question A 
	---------------------------------------------------------------------------------------------
	Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) 
	on the x-axis and returns whether they overlap. 
	As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
	---------------------------------------------------------------------------------------------

"""

def does_overlaps(a, b):

	if a[0] <= b[0] <= a[1]:
		return True

	if a[0] <= b[1] <= a[1]:
		return True

	if b[0] <= a[0] <= b[1]:
		return True

	if b[0] <= a[1] <= b[1]:
		return True

	return False





