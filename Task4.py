List of programming languages
languages = ["Python", "Java", "C#", "JavaScript", "C++"]

Ask user for input
user_lang = input("Enter a programming language to search: ").strip()

Membership testing (handling case sensitivity optionally)
Using title case to match standard formatting
if user_lang in languages:
print(f"Yes, '{user_lang}' exists in the list.")
else:
print(f"No, '{user_lang}' does not exist in the list.")