def calculate_grade(average):
 if marks >= 90:
    return "A"
 elif marks >= 75:
    return "B"
 elif marks >= 60:
    return "C"
 else:
    return "F"
if __name__ == "__main__":
    mark1 = 82
    mark2 = 90
    mark3 = 78
    mark4 = 90
    mark5 = 75
    marks= mark1+mark2+mark3+mark4+mark5
    average=marks/5
print("Total Marks:", marks)
print("Average:", average)
print("Grade:", calculate_grade(average))