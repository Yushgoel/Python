math_marks = [56, 79, 80, 89, 24, 12, 46, 67, 81, 90]
marks_above_classification = []
classification = raw_input("Please enter a number.")
classification = int(classification)

def marks_classification(classified):
	for item in math_marks:
		if item >= classified:
			marks_above_classification.append(item)
	return marks_above_classification

print marks_classification(classification)