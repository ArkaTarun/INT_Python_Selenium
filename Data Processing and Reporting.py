def process_data(data):
    """Processes raw data into a nested dictionary: {student: {subject: score}}"""
    processed = {}
    for entry in data:
        try:
            # Validate entry
            if (not isinstance(entry, tuple) or len(entry) != 3 or
                not isinstance(entry[0], str) or not isinstance(entry[1], str) or
                not isinstance(entry[2], int) or not (0 <= entry[2] <= 100)):
                raise ValueError(f"Malformed data: {entry}")
            student, subject, score = entry
            if student not in processed:
                processed[student] = {}
            processed[student][subject] = score
        except Exception as e:
            print(f"Skipping entry due to error: {e}")
    return processed

def calculate_averages(processed):
    """Calculates average score per student."""
    averages = {}
    for student, subjects in processed.items():
        try:
            scores = list(subjects.values())
            if not scores:
                raise ValueError(f"No scores for student: {student}")
            avg = sum(scores) / len(scores)
            averages[student] = avg
        except Exception as e:
            print(f"Error calculating average for {student}: {e}")
    return averages

def students_above_threshold(processed, threshold):
    """Returns list of students scoring above threshold in all subjects."""
    return [
        student
        for student, subjects in processed.items()
        if all(score > threshold for score in subjects.values())
    ]

# --- Sample Input ---
data = [
    ("John", "Math", 85),
    ("John", "English", 90),
    ("Jane", "Math", 95),
    ("Jane", "English", 80),
    ("Jake", "Math", 70),
    ("Jake", "English", 60)
]
threshold = 75

# --- Processing ---
processed = process_data(data)
print(f"Processed Data: {processed}\n")

averages = calculate_averages(processed)
print("Average Scores:")
for student, avg in averages.items():
    print(f"{student}: {avg:.1f}")
print()

above = students_above_threshold(processed, threshold)
print(f"Students scoring above {threshold} in all subjects: {above}")