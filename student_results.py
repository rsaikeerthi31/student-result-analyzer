students = [
    {"name": "Rahul", "marks": [78, 85, 90]},
    {"name": "Anita", "marks": [88, 92, 95]},
    {"name": "Kiran", "marks": [60, 65, 70]},
    {"name": "Meena", "marks": [40, 42, 38]}
]

PASS_MARK = 40

def calculate_result(student):
    marks = student["marks"]
    total = sum(marks)
    average = total / len(marks)

    subject_status = ["Pass" if m >= PASS_MARK else "Fail" for m in marks]

    if average >= 85:
        grade = "A"
    elif average >= 60:
        grade = "B"
    else:
        grade = "C"

    overall_result = "Pass" if all(m >= PASS_MARK for m in marks) else "Fail"

    return total, average, grade, overall_result, subject_status


print("STUDENT RESULT ANALYSIS\n")

topper = ""
highest_avg = 0
pass_count = 0

for s in students:
    total, avg, grade, result, subject_status = calculate_result(s)

    print(f"{s['name']}")
    print(f"  Marks: {s['marks']}")
    print(f"  Subject Status: {subject_status}")
    print(f"  Total: {total}, Avg: {avg:.2f}, Grade: {grade}, Result: {result}\n")

    if result == "Pass":
        pass_count += 1

    if avg > highest_avg:
        highest_avg = avg
        topper = s["name"]

print(f"Topper of the class: {topper}")
print(f"Class Pass Percentage: {(pass_count / len(students)) * 100:.2f}%")

