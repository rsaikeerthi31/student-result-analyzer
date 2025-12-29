students = [
    {"name": "Rahul", "marks": [78, 85, 90]},
    {"name": "Anita", "marks": [88, 92, 95]},
    {"name": "Kiran", "marks": [60, 65, 70]},
    {"name": "Meena", "marks": [40, 42, 38]}
]

def calculate_result(student):
    total = sum(student["marks"])
    average = total / len(student["marks"])

    if average >= 85:
        grade = "A"
    elif average >= 60:
        grade = "B"
    else:
        grade = "C"

    result = "Pass" if average >= 40 else "Fail"
    return total, average, grade, result

print("STUDENT RESULT ANALYSIS\n")

topper = ""
highest_avg = 0

for s in students:
    total, avg, grade, result = calculate_result(s)
    print(f"{s['name']} -> Total: {total}, Avg: {avg:.2f}, Grade: {grade}, Result: {result}")

    if avg > highest_avg:
        highest_avg = avg
        topper = s["name"]

print(f"\nTopper of the class: {topper}")
