def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0)) # Should return 212
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(37))

words = ["hello", "world", "python", "ml", "data", "science"]

wordsCapitalized = [word.capitalize() for word in words]
print(wordsCapitalized)

def classify_score(score):
    if score >= 90:
        return "Excellent"
    if score >=75:
        return "Passed"
    else:
        return "Failed"

print(classify_score(95))  # Should return "Excellent"
print(classify_score(80))  # Should return "Passed"
print(classify_score(60))  # Should return "Failed"

def square_odds(numbers):
    return [x**2 for x in numbers if x % 2 != 0]

print(square_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

students = [
    {"name": "Ana", "grade": 92},
    {"name": "Ben", "grade": 70},
    {"name": "Carlo", "grade": 85},
    {"name": "Diana", "grade": 60},
    {"name": "Earl", "grade": 78},
]

def passed_students(students):
    return [student["name"] for student in students if student["grade"] >= 75]

print(passed_students(students))