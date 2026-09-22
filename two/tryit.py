"""Average Exam Score

This program inputs three exam scores to the user and calculates the average score printed as a float and an integer.
"""
# Prompt the user for three exam scores
exam_1 = float(input("Enter your first exam score: "))
exam_2 = float(input("Enter your second exam score: "))
exam_3 = float(input("Enter your third exam score: "))

# calculate the average and print it as a float and an integer
average = (exam_1 + exam_2 + exam_3) / 3
print(float(average))
print(int(average))