def calculate_grade(average):
    if average >= 90: return "A"
    elif average >= 80: return "B"
    elif average >= 70: return "C"
    elif average >= 60: return "D"
    else: return "F"

def calculate_results(marks):
    if not marks:
        return {"total": 0, "average": 0.0, "grade": "F"}
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    return {"total": total, "average": round(average, 2), "grade": grade}

if __name__ == "__main__":
    student_marks = [85, 90, 78, 92]
    results = calculate_results(student_marks)
    print(f"Total Marks: {results['total']}")
    print(f"Average Marks: {results['average']}")
    print(f"Grade: {results['grade']}")
