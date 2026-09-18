Creating the student dictionary
student = {
"name": "John Doe",
"registration number": "SCS/002/2024",
"course": "Software Development",
"age": 19,
"marks": 82
}

Displaying each value using its corresponding key
print("\n--- Original Dictionary Values ---")
print("Name:", student["name"])
print("Registration Number:", student["registration number"])
print("Course:", student["course"])
print("Age:", student["age"])
print("Marks:", student["marks"])

Modifying the student's marks and adding a new key called 'grade'
student["marks"] = 88
student["grade"] = "A"

print("\n--- Updated Student Dictionary ---")
print(student)