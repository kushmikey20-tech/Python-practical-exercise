Creating a list of five student marks
marks = [72, 85, 60, 90, 78]

Calculations
total_marks = sum(marks)
average_mark = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)

Displaying results
print("\n--- Student Marks Summary ---")
print(f"Marks List: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Mark: {average_mark}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")