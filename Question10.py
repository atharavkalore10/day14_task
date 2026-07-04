import numpy as np

# Generate marks for 10 students and 5 subjects
marks = np.random.randint(30, 101, (10, 5))

print("Student Marks:")
print(marks)

# Total marks of each student
total = np.sum(marks, axis=1)

# Average marks of each student
average = np.mean(marks, axis=1)

print("\nTotal Marks:")
print(total)

print("\nAverage Marks:")
print(average)

# Highest scoring student
highest = np.argmax(total)

# Lowest scoring student
lowest = np.argmin(total)

print("\nHighest Scoring Student Index:", highest)
print("Marks:")
print(marks[highest])

print("\nLowest Scoring Student Index:", lowest)
print("Marks:")
print(marks[lowest])

# Overall statistics
print("\nClass Mean:", np.mean(marks))
print("Class Standard Deviation:", np.std(marks))

# Reshape (Example)
reshaped = marks.reshape(5, 10)

print("\nReshaped Array (5 x 10):")
print(reshaped)

# Top 3 students based on total marks
top3 = np.argsort(total)[-3:]

print("\nTop 3 Students Index:")
print(top3)

print("\nMarks of Top 3 Students:")
print(marks[top3])

# Comments:
# 1. Random marks generated for 10 students.
# 2. Total and average calculated using axis=1.
# 3. argmax() finds highest scorer.
# 4. argmin() finds lowest scorer.
# 5. Mean and standard deviation represent class performance.
# 6. argsort() is used to obtain top 3 students.