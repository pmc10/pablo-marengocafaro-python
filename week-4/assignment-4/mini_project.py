# Student roster list for analysis
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Sara", "score": 92, "subject": "Data"},
    {"name": "Priya", "score": 95, "subject": "Web"},
    {"name": "Mia", "score": 79, "subject": "Python"},
    {"name": "Eli", "score": 83, "subject": "Data"},
    {"name": "Alex", "score": 62, "subject": "Web"},
]

# --- 1. Find the highest score (without using max()) ---
top_score = -1
top_scorer_name = ""

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_scorer_name = student["name"]

print(f"Top scorer:      {top_scorer_name} ({top_score})")

# --- 2. Calculate the class average ---
total_score = 0

for student in students:
    total_score += student["score"]

class_average = total_score / len(students)
print(f"Class average:   {class_average:.2f}")

# --- 3. List all unique subjects ---
subjects_offered = set()

for student in students:
    subjects_offered.add(student["subject"])

print(f"Subjects offered: {subjects_offered}")

# --- 4. List students with high scores (> 75) ---
high_scorers = []

for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])

print(f"High scorers:    {high_scorers}")
